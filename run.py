import threading
import traceback


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
        from webScrap.kau import KauScrapMain
        kau_thread = threading.Thread(target=KauScrapMain.main())
        kau_thread.start()
    except Exception as error:
        saveError(str(error) + traceback.format_exc())
    
    try:
        # 상명대학교 공지
        from webScrap.smu import SmuScrapMain
        smu_thread = threading.Thread(target=SmuScrapMain.main())
        smu_thread.start()

    except Exception as error:
        saveError(str(error) + traceback.format_exc())
