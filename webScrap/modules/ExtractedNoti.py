class ExtractedNoti:
    def __init__(self, title, date, href):
        self.title = title
        self.date = date
        self.href = href
        self.preview = ''


class ExtractedNotiList:
    def __init__(self):
        self.numOfNoti = 0
        self.category = ''
        self.extractedNotiList = []
