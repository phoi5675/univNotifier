if __name__ == '__main__':
    # 항공대학교 공지
    from webScrap.kau import KauScrapMain, KauSendMail
    KauScrapMain.main()

    # 상명대학교 공지
    from webScrap.smu import SmuScrapMain, SmuSendMail
    SmuScrapMain.main()
    # SmuSendMail.main()
'''
    def saveError(error):
        from datetime import date
        today = date.today().isoformat()
        print(error)
        file = open('log.txt', 'a')

        file.writelines(today + '    ' + repr(error) + '\n\n')
        file.close()
    try:
        # 항공대학교 공지
        from webScrap.kau import KauScrapMain, KauSendMail
        KauScrapMain.main()
        #KauSendMail.main()
    except Exception as error:
        saveError(error)

    try:
        # 상명대학교 공지
        from webScrap.smu import SmuScrapMain, SmuSendMail
        SmuScrapMain.main()
        #SmuSendMail.main()
    except Exception as error:
        saveError(error)
        '''