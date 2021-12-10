# -*- coding:utf-8 -*-
import requests
from .ExtractedNoti import *
from bs4 import BeautifulSoup
from datetime import date
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


class NotiFinderElements:
    def __init__(self):
        self.attrKeyword = ''
        self.valueKeyword = ''
        # text 또는 attr 를 추출하는 방법을 명시해야 하는 경우 사용(title, date, href)
        # getText, getAttrVal, getHref 로 사용
        self.extractionMethod = 'getText'
        self.removeTagKeywords = []


class NotiFinder:
    def __init__(self):
        self.extractDate = self.findElements
        self.extractTitle = self.findElements
        self.extractHref = self.findElements

        self.fixHref = None

        self.notiFinderElements = {
            'notiTable': NotiFinderElements(),
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

    def setExtractionMethod(self, extMethod, select: str):
        self.notiFinderElements[select].extractionMethod = extMethod

    def addRemoveTagKeywords(self, removeTag, select: str):
        self.notiFinderElements[select].removeTagKeywords.append(removeTag)

    def findNotiTable(self, scrapedHtml):
        found = scrapedHtml.find(
            attrs={self.notiFinderElements['notiTable'].attrKeyword: self.notiFinderElements['notiTable'].valueKeyword}
        )
        if self.notiFinderElements['notiLine'].attrKeyword == 'tag':
            # 항공대처럼 attr 없이 tag 로만 게시물을 나눈 경우, tag 로 검색
            return found.find_all(self.notiFinderElements['notiLine'].valueKeyword)

        return found.find_all(
            attrs={self.notiFinderElements['notiLine'].attrKeyword: self.notiFinderElements['notiLine'].valueKeyword}
        )

    def deleteNotWantedTags(self, extractedTag, select: str):
        for keywords in self.notiFinderElements[select].removeTagKeywords:
            decomposedTag = extractedTag.find(keywords)
            decomposedTag.decompose()

    # TODO 버전 변경 완료 후 findElements 지우기
    def findElements(self, notiFinderElement, wrappedNotiLine, select: str):
        try:
            extractionMethod = self.notiFinderElements[select].extractionMethod
            if extractionMethod == 'getHref':
                return wrappedNotiLine.a.get(notiFinderElement[select].valueKeyword)
            else:
                found = wrappedNotiLine.find(
                    attrs={notiFinderElement[select].attrKeyword: notiFinderElement[select].valueKeyword}
                )

                self.deleteNotWantedTags(found, select)
                if extractionMethod == 'getText':
                    return found.get_text()
                elif extractionMethod == 'getAttr':
                    return found[notiFinderElement.attrKeyword]

        except AttributeError:
            return ''

    def getHref(self, wrappedNotiLine):
        try:
            return wrappedNotiLine.a.get(self.notiFinderElements['href'].valueKeyword)
        except AttributeError:
            return ''

    def getTitle(self, wrappedNotiLine):
        try:
            found = wrappedNotiLine.find(
                attrs={self.notiFinderElements['title'].attrKeyword: self.notiFinderElements['title'].valueKeyword}
            )
            self.deleteNotWantedTags(found, 'title')
            return found.get_text()
        except AttributeError:
            return ''

    def getDate(self, wrappedNotiLine):
        try:
            found = wrappedNotiLine.find(
                attrs={self.notiFinderElements['date'].attrKeyword: self.notiFinderElements['date'].valueKeyword}
            )
            self.deleteNotWantedTags(found, 'date')
            return found.get_text()
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

        # driver 를 이용하여 자바스크립트가 동적으로 페이지를 불러온 후에 웹 스크랩

        # driver = webdriver.Chrome("/Users/kangminjae/Downloads/chromedriver")
        opts = Options()
        opts.headless = True
        driver = webdriver.Firefox(options=opts, executable_path='/usr/bin/geckodriver')

        driver.get(webPage)

        time.sleep(3)  # 웹페이지를 받기 전에 텍스트를 받으면 로딩이 되지 않은 상태에서 받을 수 있음

        textHtml = driver.page_source

        # requestedHtml = requests.get(webPage)
        # textHtml = requestedHtml.text

        textHtml = removeBlank(textHtml)

        driver.quit()

        return BeautifulSoup(textHtml, 'lxml')

    def webScrap(self, notiListAll, webPageList, categoryList):
        for notiList, webPage in zip(notiListAll, webPageList):
            scrapedHtml = NotiFinder.webToLxmlClass(webPage)
            notiTable = self.findNotiTable(scrapedHtml)

            notiList.category = categoryList[webPage]

            for notiLine in notiTable:
                date = self.getDate(notiLine)

                # if date == '2021-04-02':
                if NotiFinder.isToday(date):  # 오늘 날짜와 일치하는 공지만 추가
                    title = self.getTitle(notiLine)
                    # href 에는 게시물 id 만 포함
                    href = self.getHref(notiLine)

                    notiList.extractedNotiList.append(ExtractedNoti(title, date, href))
                    notiList.numOfNoti = notiList.numOfNoti + 1
                else:
                    continue
