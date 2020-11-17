# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from .NotiFinder import NotiFinder


def addWebPageLinkToHrefList(singleNotiList, webPage):
    def addWebLinkToHref(href, webPageLink):
        return webPageLink + href

    for extractedNotiList in singleNotiList.extractedNotiList:
        extractedNotiList.href = addWebLinkToHref(extractedNotiList.href, webPage)


# addWebPageLinkToHrefList 대신 사용할 메소드 / 링크를 POST 방식으로 변경 가능하게 만듦
def addPostMethod(page, singleNotiList, webPage):
    def addWebLinkToHref(href, webPageLink):
        return webPageLink + href

    # 항공대 홈페이지의 경우 boardId 의 int 값이 str 내부에 있으므로 이를 추출해서 링크에 포함해야 함
    def extractIntBoardId(href):
        # 정규식 사용 등 다양한 방법이 있지만, 가독성 및 속도를 위해 기존 코드 사용
        return href[(href.find('(') + 1): href.find(',')]

    def extractNewKauId(page, href):
        page.postElements['bbsId'] = href[(href.find('(') + 2): href.find(',') - 2]
        page.postElements['nttId'] = href[(href.find(',') + 3): href.find(')') - 2]

    for extractedNotiList in singleNotiList.extractedNotiList:
        # 공지의 ID 값을 따로 추출 해야 하는 경우
        if page.postElements['mboardView'] is not None:
            extractedNotiList.href = extractIntBoardId(extractedNotiList.href)
        elif len(page.postElements) != 0:
            extractNewKauId(page, extractedNotiList.href)

        extractedNotiList.href = addWebLinkToHref(extractedNotiList.href, webPage)


def setTagAttribute(value, attribute, htmlTag):
    # 기존에 attr 에 value 가 있으면 기존값을 덮어씌우는 경우가 있으므로
    try:
        htmlTag[attribute] = htmlTag[attribute] + value + ";"
    except KeyError:
        htmlTag[attribute] = value + ";"


def addCategoryNotiToHtml(notiList, htmlBase):
    def addHrTag(htmlTag):
        hrTag = BeautifulSoup("<hr>", "lxml")
        htmlTag.insert_after(hrTag.hr)

    def addCategoryToHtmlListTag(category, htmlBase):
        headerTag = htmlBase.new_tag("h1")
        headerTag.string = category + " 공지사항"

        listTag = htmlBase.new_tag("ul")
        listTag['class'] = category

        setTagAttribute("font-size:22px", "style", headerTag)

        setTagAttribute("font-size:15px", "style", listTag)
        setTagAttribute("padding-left:15px", "style", listTag)  # li 태그의 들여쓰기 없애기

        htmlBase.body.append(headerTag)
        htmlBase.body.append(listTag)

    def addNotiLineToHtmlInUnorderedListTag(notiList, htmlBase):
        def addDetailsTag(notiLine, categoryDivTag):
            detailsTag = BeautifulSoup(notiLine.preview, 'lxml')

            categoryDivTag.append(detailsTag.details)

        # notiList 는 학사, 취업 등 한 섹션의 공지를 담은 리스트
        categoryDivTag = htmlBase.find("ul", class_=notiList.category)
        for i in range(notiList.numOfNoti):
            unorderedListTag = htmlBase.new_tag("li")

            notiTag = htmlBase.new_tag("a", href=notiList.extractedNotiList[i].href)
            notiTag.string = notiList.extractedNotiList[i].title

            unorderedListTag.append(notiTag)

            categoryDivTag.append(unorderedListTag)

            if notiList.extractedNotiList[i].preview != '':  # 미리보기 지원이 되지 않는 학과는 제외
                addDetailsTag(notiList.extractedNotiList[i], categoryDivTag)

        addHrTag(categoryDivTag)

    def hasNoti(notiList):
        if notiList.numOfNoti != 0:
            return True
        else:
            return False

    if hasNoti(notiList):
        addCategoryToHtmlListTag(notiList.category, htmlBase)
        addNotiLineToHtmlInUnorderedListTag(notiList, htmlBase)
    else:
        pass


def addInfoTag(infoTagToAdd, html):
    infoTagSoup = BeautifulSoup(infoTagToAdd, 'lxml')
    infoTag = infoTagSoup.p

    setTagAttribute("font-size:13px", "style", infoTag)

    html.body.append(infoTag)


def htmlToFile(html, filepath, filename):
    # 메인 파이썬이 있는 폴더 내의 html 폴더에 저장
    # html 폴더가 없는 경우, 오류 발생
    file = open(filepath + 'html/' + filename + '.html', 'w')
    file.write(str(html))

    file.close()


def isBodyTagContainsElements(html):
    if len(html.body) != 0:
        return True
    else:
        return False


def extractContentsInsideLink(notiList, notiFinder):
    def isContains(html, element):
        if html.find(element) is not None:
            return True
        else:
            return False

    def extractPreviewContentsAsString(scrapedHtml, notiFinder, notiList):
        def isNeedToFixImageLink(homepage):
            if homepage != '':
                return True
            else:
                return False

        def fixImageLink(html, homepage):
            imgTags = html.find_all('img')
            for imgTag in imgTags:
                imgTag['src'] = homepage + imgTag['src']

        def insertInPreviewTag(contextTag):
            detailsTag = BeautifulSoup("<details><summary>미리보기</summary></details>", "lxml")
            detailsTag.details.append(contextTag)

            return detailsTag.details

        foundContextTag = scrapedHtml.find(attrs={notiFinder.notiFinderElements['preview'].attrKeyword:notiFinder.notiFinderElements['preview'].valueKeyword})

        if isContains(foundContextTag, 'img') and isNeedToFixImageLink(notiList.linkForFixImg):
            fixImageLink(foundContextTag, notiList.linkForFixImg)

        notiList.extractedNotiList[i].preview = str(insertInPreviewTag(foundContextTag))

    def extractAttachments(scrapedHtml, notiFinder, notiList):
        pass

    for i in range(notiList.numOfNoti):
        scrapedHtml = NotiFinder.webToLxmlClass(notiList.extractedNotiList[i].href)

        extractPreviewContentsAsString(scrapedHtml, notiFinder, notiList)

        extractAttachments(scrapedHtml, notiFinder, notiList)
