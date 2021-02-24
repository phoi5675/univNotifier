from bs4 import BeautifulSoup


def extractDeptHref(href):
    # 학과 공지 href id 추출
    return href[(href.find(',') + 3): href.find(')') - 1]


def extractGenHref(href):
    # 항공대 일반 공지의 경우 boardId 의 int 값이 str 내부에 있으므로 이를 추출해서 링크에 포함해야 함
    # 정규식 사용 등 다양한 방법이 있지만, 가독성 및 속도를 위해 기존 코드 사용
    return href[(href.find(')') - 6): href.find(')') - 1]


def appendHref(pageLink, appendAttr):
    return pageLink + appendAttr


def findDeptHref(notiFinderElement, wrappedNotiLine, select: str):
    return wrappedNotiLine.find("td",
                                attrs={notiFinderElement[select].attrKeyword: True})[
        notiFinderElement[select].attrKeyword]


def extractGenDate(notiFinderElement, wrappedNotiLine, select: str):
    found = wrappedNotiLine.find_all(
        attrs={notiFinderElement[select].attrKeyword: notiFinderElement[select].valueKeyword}
    )
    if not found:
        return ""
    return found[1].get_text()
