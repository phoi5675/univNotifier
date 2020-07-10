# -*- coding:utf-8 -*-
from webScrap.modules.Mail import *
from webScrap.smu.const import *


def main():
    # SMTP 서버 연결
    smtp = connectSmtp(SENDERID, SENDERPWD)

    htmlDict = {}
    # html 파일 읽고 html 딕셔너리에 담기
    makeHtmlDictFromFiles(htmlDict, FILEPATH, DEPFIARY)

    # 구글 스프레드시트 불러오기
    doc = getSpreadSheet(FILEPATH + JSON, SPREADSHEETLINK)

    # 시트 선택하기
    worksheet = doc.worksheet(SHEETNAME)

    # 스프레드시트 목록에서 메일 보내기
    sendMailFromWorksheet(worksheet, htmlDict, EMAILTITLE, DEPDICT, smtp)

    # 닫기
    smtp.close()
