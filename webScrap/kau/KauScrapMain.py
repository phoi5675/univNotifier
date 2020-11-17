# -*- coding:utf-8 -*-
import copy

from webScrap.kau.KauFunc import *
from webScrap.kau.const import *
from webScrap.modules.DeleteFile import *
from webScrap.modules.NotiFinder import *
from webScrap.modules.NotiMaker import *
from webScrap.modules.Page import *
'''
from DeleteFile import *
from NotiFinder import *
from NotiMaker import *
'''


def main():
    # -------------------- 파일 삭제 -------------------- #
    # 이전에 만들어진 파일 삭제
    for html in DEPFIARY:
        deleteFileFromDirectory(FILEPATH + "html/", html + ".html")

    # -------------------- 공지 리스트 생성 -------------------- #
    genNotiListAll = list(ExtractedNotiList() for i in range(GENINT))
    genNotiFinder = NotiFinder()

    deptNotiListAll = list(ExtractedNotiList() for i in range(DEPINT))
    deptNotiFinder = NotiFinder()

    # 취업공지는 따로 생성 / 호환성을 위해 리스트로 생성
    careerNotiListAll = list(ExtractedNotiList() for i in range(len(CAREER)))
    careerNotiFinder = NotiFinder()

    # -------------------- 별도 함수 설정 (optional) -------------------- #
    genNotiFinder.fixHref = extractGenHref
    deptNotiFinder.fixHref = extractDeptHref

    # -------------------- 공지 검색 attribute / value 설정 -------------------- #
    # 읿반 공지
    genNotiFinder.setAttributeAndValue('class', 'board_list', 'notiList')
    genNotiFinder.setAttributeAndValue('tag', 'tr', 'notiLine')
    genNotiFinder.setAttributeAndValue('headers', 'board_title', 'title')
    genNotiFinder.setAttributeAndValue('headers', 'board_create', 'date')
    genNotiFinder.setAttributeAndValue('', 'href', 'href')

    # 학과 공지
    deptNotiFinder.setAttributeAndValue('id', 'notiDfTable', 'notiList')
    deptNotiFinder.setAttributeAndValue('tag', 'tr', 'notiLine')
    deptNotiFinder.setAttributeAndValue('class', 'tit', 'title')
    deptNotiFinder.setAttributeAndValue('class', 'not_m', 'date')
    deptNotiFinder.setAttributeAndValue('onclick', '*', 'href')

    # 취업 공지
    careerNotiFinder.setAttributeAndValue('class', 'black', 'notiList')
    careerNotiFinder.setAttributeAndValue('class', 'tbody', 'notiLine')
    careerNotiFinder.setAttributeAndValue('class', 'title', 'title')
    careerNotiFinder.setAttributeAndValue('class', 'reg_date', 'date')
    careerNotiFinder.setAttributeAndValue('', 'href', 'href')

    # -------------------- 공지 검색 추출 방법 설정 -------------------- #
    # 기본값 = getText
    genNotiFinder.setExtractionMethod("getHref", "href")
    deptNotiFinder.setExtractionMethod("getAttr", "href")
    deptNotiFinder.extractHref = findDeptHref
    careerNotiFinder.setExtractionMethod("getHref", "href")

    # -------------------- 공지 추출 시 하위 태그 삭제 (optional) -------------------- #
    deptNotiFinder.notiFinderElements["title"].removeTagKeywords.append("ul")

    # -------------------- 공지 스크랩 -------------------- #
    # 일반 공지 스크랩
    webScrap(genNotiFinder, genNotiListAll, GENWEB, GENWEBDICT)

    # 취업 공지 스크랩
    webScrap(careerNotiFinder, careerNotiListAll, CAREER, GENWEBDICT)

    # 학과 공지 스크랩
    webScrap(deptNotiFinder, deptNotiListAll, DEPWEB, DEPWEBDICT)

    # -------------------- href 수정 -------------------- #
    # href 수정
    # 취업 공지를 제외한 나머지 학교 / 학과 공지는 BoardId 값 따로 추출 필요
    for genNotiList, genWeb in zip(genNotiListAll, GENWEB):
        addWebPageLinkToHrefList(genNotiList, genWeb)
    for deptNotiList, depWeb, appendAttr in zip(deptNotiListAll, DEPWEB, DEPAPPARY):
        addWebPageLinkToHrefList(deptNotiList, appendHref(depWeb, appendAttr))
    # 취업 공지는 BoardId 값 추출 필요 없음
    addWebPageLinkToHrefList(careerNotiListAll[0], CAREERAPPEND[0])

    # -------------------- 공지 내용 미리보기 만들기 -------------------- #
    genNotiFinder.setAttributeAndValue("colspan", "4", "preview")
    genNotiListAll[GENWEB.index(DORM)].linkForFixImg = HOMEPAGE

    careerNotiFinder.setAttributeAndValue("data-role", "wysiwyg-content", "preview")

    deptNotiFinder.setAttributeAndValue("id", "divViewConts", "preview")

    for notiList in genNotiListAll:
        extractContentsInsideLink(notiList, genNotiFinder)

    for notiList in deptNotiListAll:
        extractContentsInsideLink(notiList, deptNotiFinder)

    for notiList in careerNotiListAll:
        extractContentsInsideLink(notiList, careerNotiFinder)

    # -------------------- 별도 notiFinder 로 생성한 공지 append (optional) -------------------- #
    # 취업 공지를 일반 공지로 넘기기
    genNotiListAll.append(careerNotiListAll[0])

    # -------------------- html 인스턴스에 공지, 정보 태그 추가 및 파일 저장 -------------------- #
    # 받은 공지를 html 인스턴스로 넘기기
    htmlBaseInString = HTMLBASE
    htmlBase = BeautifulSoup(htmlBaseInString, 'lxml')

    # 학교 일반 공지 전체 추가
    for singleCategoryNotiList in genNotiListAll:
        addCategoryNotiToHtml(singleCategoryNotiList, htmlBase)

    # 학과 공지
    for singleCategoryNotiList, filename in zip(deptNotiListAll, DEPFIARY):
        # 0. 공지가 없는 경우 루프 패스 / 이건 왜 안 넣었지
        if not isBodyTagContainsElements(htmlBase) and singleCategoryNotiList.numOfNoti == 0:
            continue
        # 1. copy 를 이용하여 일반 공지를 담은 htmlBase 를 유지한 채 htmlToSaveDeptNoti 에 htmlBase 내용 복사
        #    n 번째 루프에서는 덮어쓰기
        htmlToSaveDeptNoti = copy.copy(htmlBase)

        # 2. 한 학과의 공지를 htmlToSaveDeptNoti 에 저장
        addCategoryNotiToHtml(singleCategoryNotiList, htmlToSaveDeptNoti)

        # 3. INFOTAG 추가
        addInfoTag(INFOTAG, htmlToSaveDeptNoti)

        # 4. htmlBase 를 학과 파일로 저장
        htmlToFile(htmlToSaveDeptNoti, FILEPATH, filename)
