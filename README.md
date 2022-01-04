# univNotifier

# Introduction
대학교 공지사항을 오후 9시에 메일로 발송하는 프로그램입니다.

현재는 항공대, 상명대 공지사항을 메일로 보내고 있습니다.
# Setup
### setup은 모두 이 repository의 루트 디렉토리에서 실행합니다.

## docker setup
build docker image
```shell
docker build -f dockerfiles/Dockerfile -t scrapimg .
```
run docker container
```shell
docker run -itd --name webscrap \
    --restart=always \
    -v %cd%:/webScrap scrapimg
```

# Requirements
- __python3 (2.7.x 에서는 unicode 오류 가능성 있음)__
```shell
pip3 install -r requirements.txt
```
# Sources
- 웹 스크래핑
  - [kau.ac.kr 에의 링크 추출](https://github.com/Space4all/kau-notify)
  - [beautifulsoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- email 발송
  - [파이썬 이메일 자동화](http://hleecaster.com/python-email-automation/)
  - [html 형식으로 메일 발송](https://stackoverflow.com/questions/882712/sending-html-email-using-python)
  - [파이썬에서 구글 스프레드시트 이용](http://hleecaster.com/python-google-drive-spreadsheet-api/)
- 모듈 관리
  - [자매 폴더의 모듈 import](https://stackoverflow.com/questions/6323860/sibling-package-imports/50193944#50193944)
  
# ETC
- setup.py 가 존재해야 자매 폴더의 모듈 import 가능합니다. 없을 경우 import error 발생하며, 자세한 내용은 Sources 의 모듈 관리 링크 참고해 주세요.
- 구글 폼을 이용하지 않고, 자체 데이터베이스 및 홈페이지 제작 예정입니다.
- 개인 리눅스 서버의 cron 을 이용해서 파이썬 파일을 실행합니다.

# License
MIT License. For more information, see LICENSE.

# Known problems
- Windows docker 환경에서 docker의 메모리 과다 점유 문제가 있습니다. [여기](https://github.com/microsoft/WSL/issues/4166#issuecomment-526725261) 를 참고해서 해결 가능합니다. 또는, WSL2 기능 대신 Hyper-V 기능을 사용하여 Docker를 실행하여 해결합니다.