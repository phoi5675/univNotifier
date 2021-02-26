# -*- coding:utf-8 -*-
import copy

from webScrap.smu.const import *
from webScrap.smu.SmuNotiFinder import *
from webScrap.smu.SmuNotiMaker import *
from webScrap.modules.DeleteFile import *
from webScrap.modules.NotiFinder import *
from webScrap.modules.NotiMaker import *


def main():
    # -------------------- 파일 삭제 -------------------- #
    # 이전에 만들어진 파일 삭제
    for html in DEPFIARY:
        deleteFileFromDirectory(FILEPATH + "html/", html + ".html")

    # -------------------- 공지 리스트 생성 -------------------- #
    genNotiListAll = list(ExtractedNotiList() for i in range(GENINT))
    deptNotiListAll = list(ExtractedNotiList() for i in range(DEPINT))

    notiFinder = SmuNotiFinder()

    # -------------------- 공지 스크랩 -------------------- #
    # 일반 공지 스크랩
    notiFinder.webScrap(genNotiListAll, GENWEB, GENWEBDICT)

    # 학과 공지 스크랩
    notiFinder.webScrap(deptNotiListAll, DEPWEB, DEPWEBDICT)

    # -------------------- href 수정 -------------------- #
    # href 수정
    # 취업 공지를 제외한 나머지 학교 / 학과 공지는 BoardId 값 따로 추출 필요
    for genNotiList in genNotiListAll:
        SmuNotiMaker.addWebPageLinkToHrefList(genNotiList, GENERALNOTILINK)
    for deptNotiList, depWeb in zip(deptNotiListAll, DEPWEB):
        SmuNotiMaker.addWebPageLinkToHrefList(deptNotiList, depWeb)

    # -------------------- 공지 내용 미리보기 만들기 -------------------- #
    for notiList in genNotiListAll:
        notiList.linkForFixImg = HOMEPAGE
        SmuNotiMaker.extractContentsInsideLink(notiList, notiFinder)

    for notiList in deptNotiListAll:
        notiList.linkForFixImg = HOMEPAGE
        SmuNotiMaker.extractContentsInsideLink(notiList, notiFinder)

    # -------------------- html 인스턴스에 공지, 정보 태그 추가 및 파일 저장 -------------------- #
    # 받은 공지를 html 로 넘기기
    htmlBaseInString = HTMLBASE
    htmlBase = BeautifulSoup(htmlBaseInString, 'lxml')

    # 학교 일반 공지 전체 추가
    for singleCategoryNotiList in genNotiListAll:
        SmuNotiMaker.addCategoryNotiToHtml(singleCategoryNotiList, htmlBase)

    # 학과 공지
    for singleCategoryNotiList, filename in zip(deptNotiListAll, DEPFIARY):
        # 0. 공지가 없는 경우 루프 패스 / 이건 왜 안 넣었지
        if not SmuNotiMaker.isBodyTagContainsElements(htmlBase) and singleCategoryNotiList.numOfNoti == 0:
            continue
        # 1. copy 를 이용하여 일반 공지를 담은 htmlBase 를 유지한 채 htmlToSaveDeptNoti 에 htmlBase 내용 복사
        #    n 번째 루프에서는 덮어쓰기
        htmlToSaveDeptNoti = copy.copy(htmlBase)

        # 2. 한 학과의 공지를 htmlToSaveDeptNoti 에 저장
        SmuNotiMaker.addCategoryNotiToHtml(singleCategoryNotiList, htmlToSaveDeptNoti)

        # 3. INFOTAG 추가
        SmuNotiMaker.addInfoTag(INFOTAG, htmlToSaveDeptNoti)

        # 4. htmlBase 를 학과 파일로 저장
        SmuNotiMaker.htmlToFile(htmlToSaveDeptNoti, FILEPATH, filename)
