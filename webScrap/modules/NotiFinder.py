# -*- coding:utf-8 -*-
import requests
from .ExtractedNoti import *
from bs4 import BeautifulSoup
from datetime import date


class NotiFinderElements:
    def __init__(self):
        self.attrKeyword = ''
        self.valueKeyword = ''
        self.removeTagKeywords = []


class NotiFinder:
    def __init__(self):
        self.notiFinderElements = {
            'notiList': NotiFinderElements(),
            'notiLine': NotiFinderElements(),
            'title': NotiFinderElements(),
            'date': NotiFinderElements(),
            'href': NotiFinderElements(),
            'preview': NotiFinderElements(),
            'attachment': NotiFinderElements()
        }

    def setAttributeAndValue(self, attribute, value, select: str):
        self.notiFinderElements[select].attrKeyword = attribute
        self.notiFinderElements[select].valueKeyword = value

    def addRemoveTagKeywords(self, removeTag, select: str):
        self.notiFinderElements[select].removeTagKeywords.append(removeTag)

    def findAllWrappedNotiLine(self, scrapedHtml):
        found = scrapedHtml.find(
            attrs={self.notiFinderElements['notiList'].attrKeyword: self.notiFinderElements['notiList'].valueKeyword}
        )
        if self.notiFinderElements['notiLine'].attrKeyword == 'tag':
            # 항공대처럼 attr 없이 tag 로만 게시물을 나눈 경우, tag 로 검색
            return found.find_all(self.notiFinderElements['notiLine'].valueKeyword)

        return found.find_all(
            attrs={self.notiFinderElements['notiLine'].attrKeyword: self.notiFinderElements['notiLine'].valueKeyword}
        )

    def findElements(self, wrappedNotiLine, select: str, isReturnText=False):
        def deleteNotWantedTags(extractedTag):
            for keywords in self.notiFinderElements[select].removeTagKeywords:
                decomposedTag = extractedTag.find(keywords)
                decomposedTag.decompose()

        try:
            if select == 'href':
                return wrappedNotiLine.a.get(self.notiFinderElements[select].valueKeyword)
            else:
                found = wrappedNotiLine.find(
                    attrs={self.notiFinderElements[select].attrKeyword: self.notiFinderElements[select].valueKeyword}
                )
                deleteNotWantedTags(found)
                if isReturnText:
                    return found.get_text()
                else:
                    return found

        except AttributeError:
            return ''

    @staticmethod
    def isToday(scrapDate):
        convertedDate = scrapDate.replace('.', '-')  # . 으로 날짜 표시가 된 경우 변경 / 조금 더 좋은 방법은 나중에..
        today = date.today().isoformat()
        if convertedDate == today:
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
            date = notiFinder.findElements(notiLine, 'date', True)

            if NotiFinder.isToday(date):  # 오늘 날짜와 일치하는 공지만 추가
                title = notiFinder.findElements(notiLine, 'title', True)
                # href 에는 게시물 id 만 포함
                href = notiFinder.findElements(notiLine, 'href', True)

                notiList.extractedNotiList.append(ExtractedNoti(title, date, href))
                notiList.numOfNoti = notiList.numOfNoti + 1
            else:
                continue
