# -*- coding:utf-8 -*-
# 구글 스프레드시트 import
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# 이메일 import
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time


# 이메일 유효성 검사 함수
def is_valid(addr):
    import re
    if re.match('(^[a-zA-Z-0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', addr):
        return True
    else:
        return False


# 이메일 발송 함수
def send_mail(smtp, addr: list, subj_layout, cont_layout, attachment=None):
    # 텍스트 파일
    msg = MIMEMultipart("alternative")
    # 첨부파일이 있는 경우 mixed로 multipart 생성
    if attachment:
        msg = MIMEMultipart('mixed')
    msg["From"] = smtp.user
    msg["To"] = smtp.user
    msg["Subject"] = subj_layout
    # list 를 str 로 변환
    contents = ''
    for cont_line in cont_layout:
        contents = contents + cont_line
    text = MIMEText(contents, 'html', _charset='utf-8')
    msg.attach(text)
    # 첨부파일이 있으면
    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders
        file_data = MIMEBase("application", "octect-stream")
        file_data.set_payload(open(attachment, "rb").read())
        encoders.encode_base64(file_data)
        import os
        filename = os.path.basename(attachment)
        file_data.add_header("Content-Disposition", 'attachment', filename=('UTF-8', '', filename))
        msg.attach(file_data)

    # 메일 발송
    to_addr = [smtp.user] + addr
    smtp.sendmail(smtp.user, to_addr, msg.as_string())


def connectSmtp(senderId, senderPwd):
    # SMTP 접속을 위한 서버, 계정 설정
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465
    # 보내는 메일 계정
    SMTP_USER = senderId
    SMTP_PASSWORD = senderPwd

    # smtp로 접속할 서버 정보를 가진 클래스변수 생성
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    # 해당 서버로 로그인
    smtp.login(SMTP_USER, SMTP_PASSWORD)

    return smtp


def makeHtmlDictFromFiles(htmlDict, filepath, fileArray):
    for filename in fileArray:
        try:
            file = open(filepath + 'html/' + filename + '.html', 'r')
            htmlDict[filename] = file.readlines()
            file.close()
        except FileNotFoundError:
            pass


def getSpreadSheet(jsonWithFullPath, spreadsheetlink):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]

    jsonFileName = jsonWithFullPath
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonFileName, scope)
    gc = gspread.authorize(credentials)
    # 스프레스시트 문서 가져오기
    return gc.open_by_url(spreadsheetlink)


def sendMailFromWorksheet(worksheet, htmlDict, mailTitle, categoryKey, smtp):
    mailAddrList = worksheet.col_values(2)
    majList = worksheet.col_values(3)
    cancelSubscriptionList = worksheet.col_values(4)

    subscribers: dict = {key: [] for key in categoryKey.values()}
    # 셀의 데이터는 2행부터 시작, list 라서 i 값은 1
    for i in range(1, len(mailAddrList)):
        # 구독 취소 한 사람의 경우 루프 넘김
        if cancelSubscriptionList[i] == 'O':
            continue

        if not is_valid(mailAddrList[i]):
            print("Wrong email: " + mailAddrList[i])
            continue
        index = categoryKey[majList[i]]

        subscribers[index].append(mailAddrList[i])
    
    # 메일 발송
    for key in categoryKey.values():
        if htmlDict[key] != '' or len(subscribers[key]) > 0:
            try:
                send_mail(smtp, subscribers[key], mailTitle, htmlDict[key])
            except Exception as error:
                print(error)
