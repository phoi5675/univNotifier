class ExtractedNoti:
    def __init__(self, title, date, href):
        self.title = title
        self.date = date
        self.href = href
        self.preview = ''
        self.attachment = {}  # 첨부파일은 두 개 이상인 경우도 있으므로 "제목": "링크" 형태의 딕셔너리로 사용


class ExtractedNotiList:
    def __init__(self):
        self.numOfNoti = 0
        self.category = ''
        self.extractedNotiList = []
