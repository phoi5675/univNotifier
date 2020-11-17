BOARDID = "?search_boardId="
HOMEPAGE = "http://www.kau.ac.kr"
# 일반, 학사공지
GENERAL = "http://kau.ac.kr/page/kauspace/general_list.jsp" + BOARDID  # 일반
ACADEMIC = "http://kau.ac.kr/page/kauspace/academicinfo_list.jsp" + BOARDID  # 학사
SCHOLAR = "http://www.kau.ac.kr/page/kauspace/scholarship_list.jsp" + BOARDID  # 장학 / 대출
RESEARCH = "http://www.kau.ac.kr/page/kauspace/research_list.jsp" + BOARDID  # 산학 / 연구
EVENT = "http://www.kau.ac.kr/page/kauspace/event_list.jsp" + BOARDID  # 행사
EMPLOY = "http://www.kau.ac.kr/page/kauspace/employment_list.jsp" + BOARDID  # 모집 / 채용
DORM = "http://www.kau.ac.kr/page/web/life/community/notice_li.jsp" + BOARDID  # 기숙사
CAREER = ["http://career.kau.ac.kr/ko/community"]  # 취업 -> 양식이 다르므로 따로 추가
CAREERAPPEND = ["http://career.kau.ac.kr"]  # 취업 -> 링크 붙이기 용도

# 학과공지
DEPTPAGE = "http://college.kau.ac.kr/web/pages/"
MACH = DEPTPAGE + "gc1986b.do"  # 항우기
ELEC = DEPTPAGE + "gc23761b.do"  # 항전정
SOFT = DEPTPAGE + "gc911b.do"  # 소프트
STUF = DEPTPAGE + "gc46806b.do"  # 재료
LAWS = DEPTPAGE + "gc93464b.do"  # 교물
AVIA = DEPTPAGE + "gc61682b.do"  # 운항
BUSI = DEPTPAGE + "gc25685b.do"  # 경영
FREE = DEPTPAGE + "gc46051b.do"  # 자유
# 스마트드론 학과 모집하면 추가해야됨

# get 메서드를 사용하기 위한 attr 이어붙이기용
MACHAPP = "?bbsAuth=30&siteFlag=am_www&bbsFlag=View&bbsId=0024&currentPageNo=1&mnuId=gc1986b&nttId="  # 항우기
ELECAPP = "?bbsAuth=30&siteFlag=eie_www&bbsFlag=View&bbsId=0015&currentPageNo=&mnuId=gc23761b&nttId="  # 항전정
SOFTAPP = "?bbsAuth=30&siteFlag=sw_www&bbsFlag=View&bbsId=0032&currentPageNo=&mnuId=gc911b&nttId="  # 소프트
STUFAPP = "?bbsAuth=30&siteFlag=materials_www&bbsFlag=View&bbsId=0096&currentPageNo=1&mnuId=gc46806b&nttId="  # 재료
LAWSAPP = "?bbsAuth=30&siteFlag=attll_www&bbsFlag=View&bbsId=0048&currentPageNo=&mnuId=gc93464b&nttId="  # 교물
AVIAAPP = "?bbsAuth=30&siteFlag=hw_www&bbsFlag=View&bbsId=0003&currentPageNo=&mnuId=gc61682b&nttId="  # 운항
BUSIAPP = "?bbsAuth=30&siteFlag=biz_www&bbsFlag=View&bbsId=0056&currentPageNo=&mnuId=gc25685b&nttId="  # 경영
FREEAPP = "?bbsAuth=30&siteFlag=free_www&bbsFlag=View&bbsId=0072&currentPageNo=1&mnuId=gc46051b&nttId="  # 자유

# 학교 전체 공지 링크 리스트
GENWEB = [GENERAL, ACADEMIC, SCHOLAR, RESEARCH, EVENT, EMPLOY, DORM]

# 학과 공지 배열
DEPWEB = [MACH, ELEC, STUF, LAWS, AVIA, BUSI, FREE, SOFT]

# get 메서드를 사용하기 위한 attr 이어붙이기용 배열
DEPAPPARY = [MACHAPP, ELECAPP, STUFAPP, LAWSAPP, AVIAAPP, BUSIAPP, FREEAPP, SOFTAPP]

# 학교 전체 공지 배열 크기
GENINT = len(GENWEB)

# 학과 공지 배열 크기
DEPINT = len(DEPWEB)

# 파일 저장용 배열
DEPFIARY = ["mach", "elec", "stuf", "laws", "avia", "busi", "free", "soft"]

# 구글 스프레드시트 -> 파일 읽기
DEPDICT = {"항우기": "mach", "항전정": "elec", "소프트": "soft", "재료": "stuf",
           "교물": "laws", "운항": "avia", "경영": "busi", "자유": "free"}

# -------------------- html -------------------- #
# 학교 전체 공지 딕셔너리
GENWEBDICT = {GENERAL: "일반", ACADEMIC: "학사", SCHOLAR: "장학 / 대출", RESEARCH: "산학 / 연구",
              EVENT: "행사", EMPLOY: "모집 / 채용", DORM : "생활관", CAREER[0]: "취업"
}
# 학과 공지 딕셔너리
DEPWEBDICT = {MACH: "항공우주기계공학부", ELEC: "항공전자정보공학부", SOFT: "소프트웨어학과", STUF: "재료공학부",
              LAWS: "항공교통물류학부", AVIA: "항공운항학과", BUSI: "경영학부", FREE: "자유전공학부"
}

# HTML 파일 베이스
# <body> 태그 내부에는 공백을 포함한 어떤 str 도 포함되면 안됨!
# NotiMaker.isBodyTagContainsElements() 에서 element 로 인식해서 오류 발생
HTMLBASE = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset=\"utf-8\">
    </head>
    <body></body>
</html>
'''

# HTML 아래에 구독 신청 / 취소 등 정보를 위한 p 태그 및 신청 / 취소 링크
SUBSCRIBELINK = "https://forms.gle/WwL3GB57zbRq5PWG6"
UNSUBSCRIBELINK = "https://forms.gle/eHxyqZTD1HNA3u9SA"
MEMOSTRING = ""
MAILLINK = "phoinotifier@gmail.com"
INFOTAG = '''
<p>
다른 학우분들도 메일을 받아 볼 수 있게 해주세요! 신청은 <a href=''' + SUBSCRIBELINK + '''>여기</a> 에서 할 수 있습니다<br>
구독을 중단하고 싶은 경우 <a href=''' + UNSUBSCRIBELINK + '''>여기</a>에 메일을 적어주세요<br>
기타 문의사항은 <a href=''' + MAILLINK + '''>''' + MAILLINK + '''</a>으로 문의 바랍니다<br>
''' + MEMOSTRING + '''
</p>
'''

# -------------------- 파일 -------------------- #
# 파일 경로 / 루트 폴더까지만 절대경로로 지정
# 상대경로 사용 시 cron 및 파일 R/W 에서 IDE 실행 시에는 없던 오류가 발생할 가능성 있음
FILEPATH = "./webScrap/kau/"
# -------------------- email 발송 -------------------- #
# json 파일 이름
JSON = 'json'

# 이메일 ID / PW
SENDERID = "phoiNotifier@gmail.com"
SENDERPWD = "pwd"

# 스프레드시트 링크
SPREADSHEETLINK = "https://https://docs.google.com/spreadsheets/d/1sX2eyYgBJta8y_p0ZMCvhTto6rjBOQZoOo3gStXtg3M/edit" \
                  "#gid=534886396 "

# 시트 이름
SHEETNAME = "설문지 응답 시트1"

# email 제목
EMAILTITLE = "항공대학교 공지사항"

# -------------------- deprecated values -------------------- #
GENFIARY = ["gen", "aca", "sch", "res", "eve", "emp", "car"]
