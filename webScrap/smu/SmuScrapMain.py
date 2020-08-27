# -*- coding:utf-8 -*-
import copy

from webScrap.smu.const import *
from webScrap.modules.DeleteFile import *
from webScrap.modules.NotiFinder import *
from webScrap.modules.NotiMaker import *
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
    deptNotiListAll = list(ExtractedNotiList() for i in range(DEPINT))

    notiFinder = NotiFinder()

    # -------------------- 공지 검색 attribute / value 설정 -------------------- #
    # notiFinder attribute / value 설정
    notiFinder.setAttributeAndValue('class', 'board-thumb-wrap', 'notiList')
    notiFinder.setAttributeAndValue('class', 'board-thumb-content-wrap', 'notiLine')
    notiFinder.setAttributeAndValue('class', 'board-thumb-content-title', 'title')
    notiFinder.setAttributeAndValue('class', 'board-thumb-content-date', 'date')
    notiFinder.setAttributeAndValue('', 'href', 'href')

    notiFinder.addRemoveTagKeywords('span', 'date')

    # -------------------- 공지 스크랩 -------------------- #
    # 일반 공지 스크랩
    webScrap(notiFinder, genNotiListAll, GENWEB, GENWEBDICT)

    # 학과 공지 스크랩
    webScrap(notiFinder, deptNotiListAll, DEPWEB, DEPWEBDICT)

    # -------------------- href 수정 -------------------- #
    # href 수정
    # 취업 공지를 제외한 나머지 학교 / 학과 공지는 BoardId 값 따로 추출 필요
    for genNotiList in genNotiListAll:
        addWebPageLinkToHrefList(genNotiList, GENERALNOTILINK, False)
    for deptNotiList, depWeb in zip(deptNotiListAll, DEPWEB):
        addWebPageLinkToHrefList(deptNotiList, depWeb, False)

    # -------------------- 공지 내용 미리보기 만들기 -------------------- #
    notiFinder.setAttributeAndValue("class", "board-view-content-wrap board-view-txt", "preview")

    for notiList in genNotiListAll:
        extractContentsInsideLink(notiList, notiFinder)

    for notiList in deptNotiListAll:
        extractContentsInsideLink(notiList, notiFinder)

    # -------------------- html 인스턴스에 공지, 정보 태그 추가 및 파일 저장 -------------------- #
    # 받은 공지를 html 로 넘기기
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
