# -*- coding:utf-8 -*-
import copy

from webScrap.kau.const import *
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

    # 소프트웨어 학과 공지도 따로 생성
    softNotiListAll = list(ExtractedNotiList() for i in range(len(SOFT)))
    softNotiFinder = NotiFinder()

    # 취업공지는 따로 생성 / 호환성을 위해 리스트로 생성
    careerNotiListAll = list(ExtractedNotiList() for i in range(len(CAREER)))
    notiFinderCareer = NotiFinder()

    # -------------------- 공지 검색 attribute / value 설정 -------------------- #
    # notiFinder attribute / value 설정
    notiFinder.setAttributeAndValue('class', 'board_list', 'notiList')
    notiFinder.setAttributeAndValue('tag', 'tr', 'notiLine')
    notiFinder.setAttributeAndValue('headers', 'board_title', 'title')
    notiFinder.setAttributeAndValue('headers', 'board_create', 'date')
    notiFinder.setAttributeAndValue('', 'href', 'href')

    # notiFinder for software attribute / value 설정
    softNotiFinder.setAttributeAndValue('class', 'kboard-list', 'notiList')
    softNotiFinder.setAttributeAndValue('tag', 'tr', 'notiLine')
    softNotiFinder.setAttributeAndValue('class', 'kboard-avatar-cut-strings', 'title')
    softNotiFinder.setAttributeAndValue('class', 'kboard-list-date', 'date')
    softNotiFinder.setAttributeAndValue('', 'href', 'href')

    # notiFinder for career attribute / value 설정
    notiFinderCareer.setAttributeAndValue('class', 'black', 'notiList')
    notiFinderCareer.setAttributeAndValue('class', 'tbody', 'notiLine')
    notiFinderCareer.setAttributeAndValue('class', 'title', 'title')
    notiFinderCareer.setAttributeAndValue('class', 'reg_date', 'date')
    notiFinderCareer.setAttributeAndValue('', 'href', 'href')

    # -------------------- 공지 스크랩 -------------------- #
    # 일반 공지 스크랩
    webScrap(notiFinder, genNotiListAll, GENWEB, GENWEBDICT)

    # 취업 공지 스크랩
    webScrap(notiFinderCareer, careerNotiListAll, CAREER, GENWEBDICT)

    # 학과 공지 스크랩
    webScrap(notiFinder, deptNotiListAll, DEPWEB, DEPWEBDICT)

    # 소프트학과 공지 스크랩
    webScrap(softNotiFinder, softNotiListAll, SOFT, DEPWEBDICT)

    # -------------------- href 수정 -------------------- #
    # href 수정
    # 취업 공지를 제외한 나머지 학교 / 학과 공지는 BoardId 값 따로 추출 필요
    for genNotiList, genWeb in zip(genNotiListAll, GENWEB):
        addWebPageLinkToHrefList(genNotiList, genWeb, True)
    for deptNotiList, depWeb in zip(deptNotiListAll, DEPWEB):
        addWebPageLinkToHrefList(deptNotiList, depWeb, True)
    # 취업 공지는 BoardId 값 추출 필요 없음
    addWebPageLinkToHrefList(careerNotiListAll[0], CAREERAPPEND[0], False)
    # 소프트 공지도 BoardId 값 추출 필요 없음
    addWebPageLinkToHrefList(softNotiListAll[0], SOFT[0], False)

    # -------------------- 공지 내용 미리보기 만들기 -------------------- #
    genNotiPreviewFinder = NotiFinder()
    genNotiPreviewFinder.setAttributeAndValue("colspan", "4", "notiLine")

    deptNotiPreviewFinder = NotiFinder()
    deptNotiPreviewFinder.setAttributeAndValue("colspan", "4", "notiLine")

    careerNotiPreviewFinder = NotiFinder()
    careerNotiPreviewFinder.setAttributeAndValue("data-role", "wysiwyg-content", "notiLine")

    softNotiPreviewFinder = NotiFinder()
    softNotiPreviewFinder.setAttributeAndValue("class", "content-view", "notiLine")

    for notiList in genNotiListAll:
        extractPreviewContextTagAsString(notiList, genNotiPreviewFinder)

    for notiList in deptNotiListAll:
        if notiList.category == "경영학부":  # 경영학부 공지 세부내용은 로그인 한 사용자만 볼 수 있으므로 접근 불가
            continue
        extractPreviewContextTagAsString(notiList, deptNotiPreviewFinder)

    for notiList in careerNotiListAll:
        extractPreviewContextTagAsString(notiList, careerNotiPreviewFinder)

    for notiList in softNotiListAll:
        extractPreviewContextTagAsString(notiList, softNotiPreviewFinder)

    # -------------------- 별도 notiFinder 로 생성한 공지 append (optional) -------------------- #
    # 취업 공지를 일반 공지로 넘기기
    genNotiListAll.append(careerNotiListAll[0])
    # 소프트 공지를 일반 공지로 넘기기
    deptNotiListAll.append(softNotiListAll[0])
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
