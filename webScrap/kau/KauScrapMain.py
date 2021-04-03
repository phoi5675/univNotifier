# -*- coding:utf-8 -*-
import copy

from webScrap.kau.const import *
from webScrap.kau.KauNotiMaker import *
from webScrap.kau.KauNotiFinder import *
from webScrap.modules.DeleteFile import *
from webScrap.modules.NotiFinder import *
from webScrap.modules.NotiMaker import *


def main():
    # -------------------- 파일 삭제 -------------------- #
    # 이전에 만들어진 파일 삭제
    for html in DEPFIARY:
        deleteFileFromDirectory(FILEPATH + "html/", html + ".html")

    # -------------------- 공지 리스트 생성 -------------------- #
    # 학교 공지
    genNotiListAll = list(ExtractedNotiList() for i in range(GENINT))
    genNotiFinder = GenNotiFinder()

    # 취업 공지
    careerNotiListAll = list(ExtractedNotiList() for i in range(len(CAREER)))
    careerNotiFinder = CarNotiFinder()

    # 생활관
    # TODO 생활관 사이트 리뉴얼 되면 다시 작업해야 함
    dormNotiListAll = list(ExtractedNotiList() for i in range(len(DORM)))
    dormNotiFinder = DormNotiFinder()

    # 학부 공지
    deptNotiListAll = list(ExtractedNotiList() for i in range(DEPINT))
    deptNotiFinder = DeptNotiFinder()

    # 융합학부
    # TODO 공합융합학부는 나중에 선택자만 공지 받을 수 있게 변경하기
    smeNotiListAll = list(ExtractedNotiList() for i in range(len(SMEWEB)))
    smeNotiFinder = SmeNotiFinder()

    # -------------------- 이미지 링크 수정 -------------------- #
    for notiList in careerNotiListAll:
        notiList.linkForFixImg = CAREERAPPEND[0]

    # -------------------- 공지 스크랩 -------------------- #
    # 일반 공지 스크랩
    genNotiFinder.webScrap(genNotiListAll, GENWEB, GENWEBDICT)

    # 취업 공지 스크랩
    # careerNotiFinder.webScrap(careerNotiListAll, CAREER, GENWEBDICT)

    # 생활관 공지 스크랩
    # dormNotiFinder.webScrap(dormNotiListAll, DORM, GENWEBDICT)

    # 학과 공지 스크랩
    # deptNotiFinder.webScrap(deptNotiListAll, DEPWEB, DEPWEBDICT)

    # 공학융합 공지 스크랩
    # smeNotiFinder.webScrap(smeNotiListAll, SMEWEB, GENWEBDICT)

    # -------------------- href 수정 -------------------- #
    # href 수정
    # 취업 공지를 제외한 나머지 학교 / 학과 공지는 BoardId 값 따로 추출 필요

    for genNotiList, genWeb, appendAttr in zip(genNotiListAll, GENWEB, GENAPPARY):
        KauNotiMaker.addWebPageLinkToHrefList(genNotiList, genWeb + appendAttr)
    for deptNotiList, depWeb, appendAttr in zip(deptNotiListAll, DEPWEB, DEPAPPARY):
        KauNotiMaker.addWebPageLinkToHrefList(deptNotiList, depWeb + appendAttr)
    for smeNotiList, smeWeb in zip(smeNotiListAll, SMEWEB):
        KauNotiMaker.addWebPageLinkToHrefList(smeNotiList, SMEAPPEND[0])
    KauNotiMaker.addWebPageLinkToHrefList(dormNotiListAll[0], DORM[0])
    # 취업 공지는 BoardId 값 추출 필요 없음
    KauNotiMaker.addWebPageLinkToHrefList(careerNotiListAll[0], CAREERAPPEND[0])

    # -------------------- 일반공지 병합 -------------------- #
    # 일반공지 양이 너무 많아져서 2-3페이지로 분리됐으므로(...) 이를 한 개로 합쳐야 함
    genNotiFinder.mergeGenNoti(genNotiListAll, [1, 2])

    # -------------------- 공지 내용 미리보기 만들기 -------------------- #
    genNotiListAll[GENWEB.index(GENERAL)].linkForFixImg = IMGPAGE

    for notiList in genNotiListAll:
        KauNotiMaker.extractContentsInsideLink(notiList, genNotiFinder)

    for notiList in deptNotiListAll:
        KauNotiMaker.extractContentsInsideLink(notiList, deptNotiFinder)

    for notiList in careerNotiListAll:
        KauNotiMaker.extractContentsInsideLink(notiList, careerNotiFinder)

    for notiList in smeNotiListAll:
        KauNotiMaker.extractContentsInsideLink(notiList, smeNotiFinder)

    for notiList in dormNotiListAll:
        KauNotiMaker.extractContentsInsideLink(notiList, dormNotiFinder)

    # -------------------- 별도 notiFinder 로 생성한 공지 append (optional) -------------------- #
    # 취업 공지를 일반 공지로 넘기기
    genNotiListAll.append(careerNotiListAll[0])

    # 공학융합 공지 넘기기
    for smeNotiList in smeNotiListAll:
        genNotiListAll.append(smeNotiList)

    # 기숙사 공지 넘기기
    genNotiListAll.append(dormNotiListAll[0])
    # -------------------- html 인스턴스에 공지, 정보 태그 추가 및 파일 저장 -------------------- #
    # 받은 공지를 html 인스턴스로 넘기기
    htmlBaseInString = HTMLBASE
    htmlBase = BeautifulSoup(htmlBaseInString, 'lxml')

    # 학교 일반 공지 전체 추가
    for singleCategoryNotiList in genNotiListAll:
        NotiMaker.addCategoryNotiToHtml(singleCategoryNotiList, htmlBase)

    # 학과 공지
    for singleCategoryNotiList, filename in zip(deptNotiListAll, DEPFIARY):
        # 0. 공지가 없는 경우 루프 패스 / 이건 왜 안 넣었지
        if not NotiMaker.isBodyTagContainsElements(htmlBase) and singleCategoryNotiList.numOfNoti == 0:
            continue
        # 1. copy 를 이용하여 일반 공지를 담은 htmlBase 를 유지한 채 htmlToSaveDeptNoti 에 htmlBase 내용 복사
        #    n 번째 루프에서는 덮어쓰기
        htmlToSaveDeptNoti = copy.copy(htmlBase)

        # 2. 한 학과의 공지를 htmlToSaveDeptNoti 에 저장
        NotiMaker.addCategoryNotiToHtml(singleCategoryNotiList, htmlToSaveDeptNoti)

        # 3. INFOTAG 추가
        NotiMaker.addInfoTag(INFOTAG, htmlToSaveDeptNoti)

        # 4. htmlBase 를 학과 파일로 저장
        NotiMaker.htmlToFile(htmlToSaveDeptNoti, FILEPATH, filename)
