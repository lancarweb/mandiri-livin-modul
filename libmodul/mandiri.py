from .driver.driver import DriverChrome
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()
from .livin_request.mandirilivin import Livin

class Mandiri(DriverChrome):
    def __init__(self):
        super().__init__()

    def login(self, **kwargs):
        self.driver.get(os.environ["BASE_URL"])

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
        cookie_dict = []
        for cookie in self.driver.get_cookies():
            pair_cookies = ("{}={}".format(cookie["name"], cookie["value"]))
            cookie_dict.append(pair_cookies)

        self.cookies_ = (";".join(cookie_dict))
        # print(self.cookies_)

    def get_balance(self):
        balance = Livin(self.cookies_)
        return balance.livin_balance()

    def mutasi(self, accountNo, fromDate, toDate, transactionType, keyWord):
        mutasi = Livin(self.cookies_)
        
        # # data params
        # accountNo = ""
        # fromDate = ""
        # toDate = ""
        # transactionType = ""
        # keyWord = ""
        
        return mutasi.livin_mutasi(accountNo, fromDate, toDate, transactionType, keyWord)

    def logout_request(self):
        logout = Livin(self.cookies_)
        logout.livin_logout()

    def logout(self):
        while True:
            sleep(1)
            try:
                self.driver.find_element(self.By.XPATH, '//i[@class="mdr-logout dropdown-menu-icon"]').click()
                break
            except:
                pass

        while True:
            sleep(1)
            try:
                self.driver.find_element(self.By.XPATH, '//*[@id="btnCancelReg"]').click()
                break
            except:
                pass

        self.driver.switch_to.default_content() # end-frame

    def driver_quit(self):
        self.driver.quit()

# if __name__ == '__main__':
#     app = Mandiri()
#     # auth *
#     app.login(username="shodiq0604", password="Muzaki334") # Login|selenium
#     app.getcookies() # Create|Cookies

#     # get balance
#     input('Get balance')
#     bal = app.get_balance()
#     print(bal)
    
#     # get mutasi
#     input('Get Mutasi')
#     mut = app.mutasi("1350015688359", "1648746000000", "1649869200000", "D", "")
#     print(mut)

#     # Logout
#     input('Logout.')
#     app.logout_request()

#     # Quit-Sel
#     input('Quit-Sel')
#     app.driver_quit()