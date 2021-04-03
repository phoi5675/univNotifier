# -*- coding:utf-8 -*-
from webScrap.modules.NotiFinder import *


class GenNotiFinder(NotiFinder):
    def __init__(self):
        super().__init__()
        # 공지 검색을 위한 html attr / values
        self.setAttributeAndValue(attribute='class', value='table_board', select='notiTable')
        self.setAttributeAndValue(attribute='tag', value='tr', select='notiLine')
        self.setAttributeAndValue(attribute='class', value='tit', select='title')
        self.setAttributeAndValue(attribute='class', value='not_m', select='date')
        self.setAttributeAndValue(attribute='onclick', value='*', select='href')

        # 텍스트에서 불피요한 태그 삭제
        self.addRemoveTagKeywords(removeTag='ul', select='title')

        # 미리보기 설정
        self.setAttributeAndValue("id", "divViewConts", "preview")

    def getHref(self, wrappedNotiLine):
        try:
            found = wrappedNotiLine.find(
                attrs={self.notiFinderElements['title'].attrKeyword, self.notiFinderElements['title'].valueKeyword}
            )
            href = found.get(self.notiFinderElements['href'].attrKeyword)
            if href is None:
                href = found.a.get(self.notiFinderElements['href'].attrKeyword)
            # 링크 수정은 나중에
            return href[(href.find(')') - 6): href.find(')') - 1]

        except AttributeError:
            return ''

    def getTitle(self, wrappedNotiLine):
        return super().getTitle(wrappedNotiLine)

    def getDate(self, wrappedNotiLine):
        found = wrappedNotiLine.find_all(
            attrs={self.notiFinderElements['date'].attrKeyword: self.notiFinderElements['date'].valueKeyword}
        )
        if not found:
            return ""
        return found[1].get_text()

    def mergeGenNoti(self, notiListAll, indexAry):
        for idx in indexAry:
            while len(notiListAll[idx].extractedNotiList) > 0:
                notiListAll[0].extractedNotiList.append(notiListAll[idx].extractedNotiList.pop())
                notiListAll[idx].numOfNoti -= 1
                notiListAll[0].numOfNoti += 1


class DeptNotiFinder(NotiFinder):
    def __init__(self):
        super().__init__()
        # 공지 검색을 위한 html attr / values
        self.setAttributeAndValue(attribute='id', value='notiDfTable', select='notiTable')
        self.setAttributeAndValue(attribute='tag', value='tr', select='notiLine')
        self.setAttributeAndValue(attribute='class', value='tit', select='title')
        self.setAttributeAndValue(attribute='class', value='not_m', select='date')
        self.setAttributeAndValue(attribute='onclick', value='*', select='href')

        # 텍스트에서 불피요한 태그 삭제
        self.addRemoveTagKeywords(removeTag='ul', select='title')

        # 미리보기 설정
        self.setAttributeAndValue(attribute="id", value="divViewConts", select="preview")

    def getHref(self, wrappedNotiLine):
        try:
            href = wrappedNotiLine.find("td",
                                        attrs={self.notiFinderElements['href'].attrKeyword: True})[
                self.notiFinderElements['href'].attrKeyword]
            return href[(href.find(',') + 3): href.find(')') - 1]
        except AttributeError:
            return ''

    def getTitle(self, wrappedNotiLine):
        return super().getTitle(wrappedNotiLine)

    def getDate(self, wrappedNotiLine):
        found = wrappedNotiLine.find(
            attrs={self.notiFinderElements['date'].attrKeyword: self.notiFinderElements['date'].valueKeyword}
        )
        if not found:
            return ""
        return found.get_text()


class CarNotiFinder(NotiFinder):
    def __init__(self):
        super().__init__()
        # 공지 검색을 위한 html attr / values
        self.setAttributeAndValue(attribute='class', value='black', select='notiTable')
        self.setAttributeAndValue(attribute='class', value='tbody', select='notiLine')
        self.setAttributeAndValue(attribute='class', value='title', select='title')
        self.setAttributeAndValue(attribute='class', value='reg_date', select='date')
        self.setAttributeAndValue(attribute='', value='href', select='href')

        # 미리보기 설정
        self.setAttributeAndValue(attribute="data-role", value="wysiwyg-content", select="preview")

    def getHref(self, wrappedNotiLine):
        return super().getHref(wrappedNotiLine)

    def getTitle(self, wrappedNotiLine):
        return super().getTitle(wrappedNotiLine)

    def getDate(self, wrappedNotiLine):
        return super().getDate(wrappedNotiLine)


class SmeNotiFinder(NotiFinder):
    def __init__(self):
        super().__init__()
        # 공지 검색을 위한 html attr / values
        self.setAttributeAndValue(attribute='class', value='table_board', select='notiTable')
        self.setAttributeAndValue(attribute='tag', value='tr', select='notiLine')
        self.setAttributeAndValue(attribute='class', value='tit', select='title')
        self.setAttributeAndValue(attribute='class', value='date', select='date')
        self.setAttributeAndValue(attribute='', value='href', select='href')

        # 텍스트에서 불피요한 태그 삭제
        self.addRemoveTagKeywords(removeTag='ul', select='title')

        # 미리보기 설정
        self.setAttributeAndValue(attribute="class", value="view_conts", select="preview")

    def getHref(self, wrappedNotiLine):
        href = super().getHref(wrappedNotiLine)
        return href.replace('..', '')

    def getTitle(self, wrappedNotiLine):
        return super().getTitle(wrappedNotiLine)

    def getDate(self, wrappedNotiLine):
        return super().getDate(wrappedNotiLine)


class DormNotiFinder(NotiFinder):
    def __init__(self):
        super().__init__()
        # 공지 검색을 위한 html attr / values
        self.setAttributeAndValue(attribute='class', value='board_list', select='notiTable')
        self.setAttributeAndValue(attribute='tag', value='tr', select='notiLine')
        self.setAttributeAndValue(attribute='headers', value='board_title', select='title')
        self.setAttributeAndValue(attribute='headers', value='board_create', select='date')
        self.setAttributeAndValue(attribute='href', value='', select='href')

        # 미리보기 설정
        self.setAttributeAndValue(attribute="colspan", value="4", select="preview")

    def getHref(self, wrappedNotiLine):
        try:
            href = wrappedNotiLine.find("a")[self.notiFinderElements['href'].attrKeyword]
            return href[(href.find('(') + 1): href.find(',')]
        except AttributeError:
            return ''

    def getTitle(self, wrappedNotiLine):
        return super().getTitle(wrappedNotiLine)

    def getDate(self, wrappedNotiLine):
        return super().getDate(wrappedNotiLine)
