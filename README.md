# univNotifier
대학교 공지사항을 오후 9시에 메일로 발송하는 프로그램입니다.

vnev 및 setup.py 가 존재해야 자매 폴더의 모듈을 import 가능합니다. 없을 경우 import error 발생하며, 자세한 내용은 Sources 의 모듈 관리 링크 참고


현재는 항공대, 상명대 공지사항을 메일로 보내고 있습니다.


개인 리눅스 서버의 cron 을 이용해서 파이썬 파일을 실행합니다
# Requirements
- python3 (2.7.x 에서는 unicode 오류 가능성 있음)
- requests
- datetime
- bs4 (Beautifulsoup)
- gspread
- oauth2client
- email
- smtplib

# Sources
- 웹 스크래핑
  - https://github.com/Space4all/kau-notify (kau.ac.kr 에서 board_id 를 이용하여 페이지 이동하는 부분)
  - https://www.crummy.com/software/BeautifulSoup/bs4/doc/ (beautifulsoup documentation)
- email 발송
  - http://hleecaster.com/python-email-automation/ (파이썬 이메일 자동화)
  - https://stackoverflow.com/questions/882712/sending-html-email-using-python (html 형식으로 메일 발송)
  - http://hleecaster.com/python-google-drive-spreadsheet-api/ (파이썬에서 구글 스프레드시트 이용)
- 모듈 관리
  - https://stackoverflow.com/questions/6323860/sibling-package-imports/50193944#50193944 (자매 폴더의 모듈 import)
  
# License
MIT License. For more information, see LICENSE.

# Changelog
- 20.07.10.
  - 항공대, 상명대 공지알리미에 쓰는 모듈 통합(modules 폴더 내의 파일)
  - cron 에서 ScrapMain.py 와 SendMail.py 각각 실행하는 방법에서 루트 폴더의 run.py 를 이용하여 공지알리미를 모두 한 번에 실행하게 변경
