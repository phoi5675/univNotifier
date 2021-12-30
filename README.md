# univNotifier
대학교 공지사항을 오후 9시에 메일로 발송하는 프로그램입니다.

venv 및 setup.py 가 존재해야 자매 폴더의 모듈 import 가능합니다. 없을 경우 import error 발생하며, 자세한 내용은 Sources 의 모듈 관리 링크 참고


현재는 항공대, 상명대 공지사항을 메일로 보내고 있습니다.

구글 폼을 이용하지 않고, 자체 데이터베이스 및 홈페이지 제작 예정입니다.


개인 리눅스 서버의 cron 을 이용해서 파이썬 파일을 실행합니다
# Setup
## docker setup
build docker image
```shell
docker build . -t scrapimg
```
run docker container
```shell
docker run -itd --name webscrap \
    --restart=always \
    -v %cd%:/webScrap scrapimg
```
## setup cron
```shell
crontab -e
```
## etc
아래의 쉘 스크립트를 이용하여,
- CRLF -> LF 변환
- geckodriver 설치

를 진행합니다
```shell
sh additional_script.sh
```
를 이용하여, 아래의 코드를 추가합니다.
```shell
30 19 * * * sh /webScrap/scrap.sh
00 21 * * * sh /webScrap/sendMail.sh
```
메일 스크랩, 발송 시간 기준에 맞춰 cron을 설정합니다.

cron service를 시작합니다.
```shell
service cron start
```

# Requirements
- python3 (2.7.x 에서는 unicode 오류 가능성 있음)
```shell
pip3 install -r requirements.txt
```
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

# Known problems
- Windows docker 환경에서 docker의 메모리 과다 점유 문제가 있습니다. [여기](https://github.com/microsoft/WSL/issues/4166#issuecomment-526725261) 를 참고해서 해결 가능합니다.