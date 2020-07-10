# -*- coding:utf-8 -*-
import requests
from .ExtractedNoti import *
from bs4 import BeautifulSoup
from datetime import date


class NotiFinder:
    def __init__(self):
        self.notiListWrapperAttribute = ''
        self.notiListWrapperValue = ''

        self.notiLineWrapperAttribute = ''
        self.notiLineWrapperValue = ''

        self.titleAttribute = ''
        self.titleValue = ''

        self.dateAttribute = ''
        self.dateValue = ''

        self.hrefAttribute = ''
        self.hrefValue = ''

    def setAttributeAndValue(self, attribute, value, select: str):
        if select == 'notiList':
            self.notiListWrapperAttribute = attribute
            self.notiListWrapperValue = value
        elif select == 'notiLine':
            self.notiLineWrapperAttribute = attribute
            self.notiLineWrapperValue = value
        elif select == 'title':
            self.titleAttribute = attribute
            self.titleValue = value
        elif select == 'date':
            self.dateAttribute = attribute
            self.dateValue = value
        elif select == 'href':
            self.hrefAttribute = attribute
            self.hrefValue = value

    def findAllWrappedNotiLine(self, scrapedHtml):
        found = scrapedHtml.find(attrs={self.notiListWrapperAttribute: self.notiListWrapperValue})
        return found.find_all(self.notiLineWrapperValue)

    def findTitleInString(self, wrappedNotiLine):
        try:
            foundTitleTag = wrappedNotiLine.find(attrs={self.titleAttribute: self.titleValue})

            resultTitle = foundTitleTag.get_text()
            return resultTitle
        except AttributeError:
            return ''

    def findDateInString(self, wrappedNotiLine):
        try:
            foundDateTag = wrappedNotiLine.find(attrs={self.dateAttribute: self.dateValue})
            if foundDateTag.span:
                foundDateTag.span.clear()

            resultDate = foundDateTag.get_text()
            return resultDate
        except AttributeError:
            return ''

    def findHrefInString(self, wrappedNotiLine):
        try:
            return wrappedNotiLine.a.get(self.hrefValue)
        except AttributeError:
            return ''

    @staticmethod
    def isToday(scrapDate):
        today = date.today().isoformat()
        if scrapDate == today:
            return True
        else:
            return False

    @staticmethod
    def webToLxmlClass(webPage):
        def removeBlank(html):
            html = html.replace("\t", "")
            html = html.replace("\n", "")
            html = html.replace("\r", "")

            return html

        requestedHtml = requests.get(webPage)
        textHtml = requestedHtml.text

        textHtml = removeBlank(textHtml)

        return BeautifulSoup(textHtml, 'lxml')


def webScrap(notiFinder, notiListAll, webPageList, categoryList):
    for notiList, webPage in zip(notiListAll, webPageList):
        scrapedHtml = NotiFinder.webToLxmlClass(webPage)
        notiLines = notiFinder.findAllWrappedNotiLine(scrapedHtml)

        notiList.category = categoryList[webPage]

        for notiLine in notiLines:
            date = notiFinder.findDateInString(notiLine)

            if NotiFinder.isToday(date):  # 오늘 날짜와 일치하는 공지만 추가
                title = notiFinder.findTitleInString(notiLine)
                # href 에는 게시물 id 만 포함
                href = notiFinder.findHrefInString(notiLine)

                notiList.extractedNotiList.append(ExtractedNoti(title, date, href))
                notiList.numOfNoti = notiList.numOfNoti + 1
            else:
                continue
