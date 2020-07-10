if __name__ == '__main__':
    # 항공대학교 공지
    from webScrap.kau import KauScrapMain, KauSendMail
    KauScrapMain.main()
    KauSendMail.main()

    # 상명대학교 공지
    from webScrap.smu import SmuScrapMain, SmuSendMail
    SmuScrapMain.main()
    SmuSendMail.main()
