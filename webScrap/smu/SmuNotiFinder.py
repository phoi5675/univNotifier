# -*- coding:utf-8 -*-
from webScrap.modules.NotiFinder import *


class SmuNotiFinder(NotiFinder):
    def __init__(self):
        super().__init__()

        self.setAttributeAndValue(attribute='class', value='board-thumb-wrap', select='notiTable')
        self.setAttributeAndValue(attribute='class', value='board-thumb-content-wrap', select='notiLine')
        self.setAttributeAndValue(attribute='class', value='board-thumb-content-title', select='title')
        self.setAttributeAndValue(attribute='class', value='board-thumb-content-date', select='date')
        self.setAttributeAndValue(attribute='', value='href', select='href')

        # 불필요한 태그 제거
        self.addRemoveTagKeywords(removeTag='span', select='date')

        # 미리보기
        self.setAttributeAndValue(attribute="class", value="board-view-content-wrap board-view-txt", select="preview")

    def getHref(self, wrappedNotiLine):
        return super().getHref(wrappedNotiLine)

    def getTitle(self, wrappedNotiLine):
        return super().getTitle(wrappedNotiLine)

    def getDate(self, wrappedNotiLine):
        return super().getDate(wrappedNotiLine)
