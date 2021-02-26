import threading


if __name__ == '__main__':
    def saveError(error):
        from datetime import date
        today = date.today().isoformat()
        print(error)
        file = open('./log.txt', 'a')

        file.writelines(today + '    ' + repr(error) + '\n\n')
        file.close()
    try:
        # 항공대학교 공지
        from webScrap.kau import KauSendMail
        kau_thread = threading.Thread(target=KauSendMail.main())
        kau_thread.start()

    except Exception as error:
        saveError(error)

    try:
        # 상명대학교 공지
        from webScrap.smu import SmuSendMail
        smu_thread = threading.Thread(target=SmuSendMail.main())
        smu_thread.start()

    except Exception as error:
        saveError(error)
