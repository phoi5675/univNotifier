# univNotifier
대학교 공지사항을 오후 9시에 메일로 발송하는 프로그램입니다.

venv 및 setup.py 가 존재해야 자매 폴더의 모듈 import 가능합니다. 없을 경우 import error 발생하며, 자세한 내용은 Sources 의 모듈 관리 링크 참고


현재는 항공대, 상명대 공지사항을 메일로 보내고 있습니다.


개인 리눅스 서버의 cron 을 이용해서 파이썬 파일을 실행합니다
# Requirements
- python3 (2.7.x 에서는 unicode 오류 가능성 있음)
- datetime
- bs4 (Beautifulsoup)
- gspread
- oauth2client
- email
- smtplib
- selenium
- gecko driver
- Firefox
- time
- ~~requests~~ (selenium 사용으로 deprecated)

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
- 20.07.13
  - run.py 에서 try except 문을 학교 별로 나누고, except 문에서는 오류를 log.txt 에 저장
  - NotiFinder 에서 findAllWrappedNotiLines 의 검색을 value 만 이용하는 방식에서 attr{key: value} 로 검색하는 방법으로 변경
  - 상명대의 공지 라인을 검색하는 키워드 변경
  - 항공대의 취업 공지를 제외한 나머지 학교 및 학과 공지 라인의 검색 방식을 attr 검색 방식에서 tag 검색 방식으로 변경
  - findAllWrappedNotiLine 에서 self.notiLineWrapperAttribute 가 'tag' 인 경우 find_all(attrs{key: value}) 방식이 아닌 find_all(tag) 방식을 이용할 수 있게 변경
- 20.08.12
  - NotiFinder 클래스의 notiList, notiLine, date, title, href 의 html tag 검색에서 쓰이는 attribute, value 등 중복 변수를 NotiFinderElements 라는 클래스를 생성하여 제거
  - NotiFinder 클래스에서 비슷한 역할을 하는 find* 메서드를 하나로 통합
  - 태그의 하위 태그가 여러 개 일 때, 이들을 제거 할 수 있는 메서드 추가
  - 항공대학교 소프트웨어학과 지원
- 20.08.18
  - 미리보기 기능 추가
- 20.08.27
  - NotiFinder class 에 preview, attachment 추가
  - NotiMaker.extractPreviewContentsAsString 메서드를 extractContentsInsideLink 로 리팩터링 및 extractAttachments 추가
  - extractAttachments 메서드는 추후 세부화 예정
  - 기타 변수 이름 및 함수 이름 변경
- 20.09.22
  - 구글 스프레드시트에서 시간 당 읽기 횟수 초과로 인한 메일 주소 읽기 및 발송 실패 오류 수정
- 20.09.23
  - 항공대 생활관 추가
  - 미리보기에서 이미지 링크 수정 방식을 함수 인자로 홈페이지를 받는 방식에서 ExtractedNotiList 의 멤버 변수 linkForFixImg 로 변경
- 20.11.16
- 웹스크랩 방식 변경 request -> webdriver
  - Dependencies 추가
    - Selenium
    - Gecko driver
    - Firefox / chrome
  - 항공대 학과 공지 지원
  - 항공대 함수 일부 모듈화(모듈화 함수 저장용 파일 추가)
    - 링크 추출 함수
  - 공지 검색 추출 방법 변경 -> boolean 사용 없애고 get* string 별도 설정
  - 메일 전송 파일과 스크랩 파일 분리
- 20.11.24
  - webToXmlClass 에서 웹 페이지 로딩이 되지 않아 html을 추출할 때 제대로 추출되지 않는 오류 수정(time.sleep() 사용)
  - Dependency 추가
    - time
- 21. 2.24
  - 항공대 홈페이지 리뉴얼로 인한 스크랩 방식 일부 변경
