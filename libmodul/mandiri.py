# from http import cookies
from curses import curs_set
from .driver.driver import DriverChrome
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()
from .livin_request.mandirilivin import Livin
import time
import datetime
import sqlite3

class MandiriAuth(DriverChrome):
    def __init__(self):
        super().__init__()

    def login(self, **kwargs):
        # print(kwargs)
        # DriverChrome.__init__(self)

        # self.driver.get(os.environ["BASE_URL"])
        self.driver.get('https://ibank.bankmandiri.co.id/retail3/')

        while True:
            sleep(1)
            try:
                self.driver.switch_to.frame("mainFrame") # start-frame
                self.driver.find_element(self.By.XPATH, '//input[@id="userid_sebenarnya"]').send_keys('{}'.format(kwargs["username"]))
                self.driver.find_element(self.By.XPATH, '//input[@id="pwd_sebenarnya"]').send_keys('{}'.format(kwargs["password"]))
                sleep(2)
                self.driver.find_element(self.By.XPATH, '//button[@id="btnSubmit"]').click()

                break
            except:
                pass

    def getcookies(self):
        err_count = 1
        while True:
            sleep(1)
            if 5 == err_count:
                break
            try:
                errsession = self.driver.find_element(self.By.XPATH, '//*[@class="text-center alert-text ns-index ns-box ns-bar ns-effect-slidetop ns-type-error ns-show"]').text
                break
            except:
                errsession = ''

            err_count += 1

        if errsession == '':
            cookie_dict = []
            for cookie in self.driver.get_cookies():
                pair_cookies = ("{}={}".format(cookie["name"], cookie["value"]))
                cookie_dict.append(pair_cookies)

            # get cookies_
            cookies_ = (";".join(cookie_dict))
            
            # database
            db = sqlite3.connect(os.getcwd()+"/dbcookies/dbcookies.db")
            cursor = db.cursor()
            query = "UPDATE cookies SET cookie = '{}' WHERE id=1".format(str(cookies_))
            cursor.execute(query)
            db.commit()
            db.close()

        else:
            return (f"{errsession}")

    def driver_quit(self):
        self.driver.quit()

class MandiriLivin:
    def __init__(self):
        # print(cookies_)
        self
    
    def get_balance(self):
        db = sqlite3.connect(os.getcwd()+"/dbcookies/dbcookies.db")
        cursor = db.cursor()
        query = "SELECT * FROM cookies"
        results = cursor.execute(query)
        results = [result[1] for result in results]
        db.close()

        balance = Livin(results[0])
        return balance.livin_balance()

    def mutasi(self, accountNo, fromDate, toDate, transactionType, keyWord):

        # timestamp converter
        fromDate = time.mktime(datetime.datetime.strptime(fromDate, "%d/%m/%Y %H:%M:%S").timetuple())
        toDate = time.mktime(datetime.datetime.strptime(toDate, "%d/%m/%Y %H:%M:%S").timetuple())

        fromDate = (str(fromDate).split('.')[0]+'000')
        toDate = (str(toDate).split('.')[0]+'000')
        
        # mutasi
        db = sqlite3.connect(os.getcwd()+"/dbcookies/dbcookies.db")
        cursor = db.cursor()
        query = "SELECT * FROM cookies"
        results = cursor.execute(query)
        results = [result[1] for result in results]
        db.close()

        mutasi = Livin(results[0])
        
        return mutasi.livin_mutasi(accountNo, fromDate, toDate, transactionType, keyWord)

    def logout_request(self):
        db = sqlite3.connect(os.getcwd()+"/dbcookies/dbcookies.db")
        cursor = db.cursor()
        query = "SELECT * FROM cookies"
        results = cursor.execute(query)
        results = [result[1] for result in results]
        db.close()

        logout = Livin(results[0])
        logout.livin_logout()

    # def logout(self):
    #     while True:
    #         sleep(1)
    #         try:
    #             self.driver.find_element(self.By.XPATH, '//i[@class="mdr-logout dropdown-menu-icon"]').click()
    #             break
    #         except:
    #             pass

    #     while True:
    #         sleep(1)
    #         try:
    #             self.driver.find_element(self.By.XPATH, '//*[@id="btnCancelReg"]').click()
    #             break
    #         except:
    #             pass

    #     self.driver.switch_to.default_content() # end-frame