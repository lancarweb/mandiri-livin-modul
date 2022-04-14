from driver.driver import DriverChrome
from time import sleep
from dotenv import load_dotenv
import os
load_dotenv()

class MandiriLivin(DriverChrome):
    def __init__(self, username, password, account):
        super().__init__()

        # variable-login
        self.username = username
        self.password = password
        self.account = account

    def login(self):
        self.driver.get(os.environ["BASE_URL"])

        while True:
            sleep(1)
            try:
                self.driver.switch_to.frame("mainFrame") # start-frame
                self.driver.find_element(self.By.XPATH, '//input[@id="userid_sebenarnya"]').send_keys(f'{self.username}')
                self.driver.find_element(self.By.XPATH, '//input[@id="pwd_sebenarnya"]').send_keys(f'{self.password}')
                sleep(2)
                self.driver.find_element(self.By.XPATH, '//button[@id="btnSubmit"]').click()

                break
            except:
                pass

    def get_debit(self):
        # select Account|debit|by|rekening
        while True:
            sleep(1)
            try:
                self.driver.find_element(self.By.XPATH, '//*[text()="{}"]'.format(self.account)).click() # click account | rek
                break
            except:
                pass

        # filter|debit|from
        while True:
            sleep(1)
            try:
                self.driver.find_element(self.By.XPATH, '//input[@id="fromDate"]').click()
                select = self.Select(self.driver.find_element(self.By.XPATH, '//select[@class="ui-datepicker-month"]'))
                sleep(0.5)
                select.select_by_visible_text("Apr")
                select = self.Select(self.driver.find_element(self.By.XPATH, '//select[@class="ui-datepicker-year"]'))
                sleep(0.5)
                select.select_by_visible_text("2022")
                tabel_cal = self.driver.find_element(self.By.XPATH, '//table[@class="ui-datepicker-calendar"]')
                sleep(0.5)
                tabel_cal.find_element(self.By.XPATH, '//*[text()="1"]').click()

                break
            except:
                pass

        # filter|debit|to
        while True:
            sleep(1)
            try:
                self.driver.find_element(self.By.XPATH, '//input[@id="toDate"]').click()
                select = self.Select(self.driver.find_element(self.By.XPATH, '//select[@class="ui-datepicker-month"]'))
                sleep(0.5)
                select.select_by_visible_text("Apr")
                select = self.Select(self.driver.find_element(self.By.XPATH, '//select[@class="ui-datepicker-year"]'))
                sleep(0.5)
                select.select_by_visible_text("2022")
                tabel_cal = self.driver.find_element(self.By.XPATH, '//table[@class="ui-datepicker-calendar"]')
                sleep(0.5)
                tabel_cal.find_element(self.By.XPATH, '//*[text()="14"]').click()

                break
            except:
                pass

        # TypeTransaction
        while True:
            sleep(0.5)
            try:
                self.driver.find_element(self.By.XPATH, '//*[@id="s2id_transactionTypes"]').click()
                break
            except:
                pass
        
        # type
        type_transaction = 'Kredit'
        if 'Kredit' == type_transaction:
            self.driver.find_element(self.By.XPATH, '//li[@class="select2-results-dept-0 select2-result select2-result-selectable"]').click()
        elif 'Debit' == type_transaction:
            self.driver.find_element(self.By.XPATH, '//li[@class="select2-results-dept-0 select2-result select2-result-selectable select2-highlighted"]').click()

        # search|filter|debit
        sleep(0.5)
        self.driver.find_element(self.By.XPATH, '//a[@id="btnSearch"]').click()

        # check 6 month|error
        err = 1
        while True:
            sleep(1)
            if 3 == err:
                six_err = False
                break
            try:
                six_err = self.driver.find_element(self.By.XPATH, '//*[@class="text-center alert-text ns-index ns-box ns-bar ns-effect-slidetop ns-type-error ns-show"]')
                break
            except:
                pass
            
            err+=1

        if six_err:
            print(six_err.text)

        else:
            print(six_err)

            # parse|data|debit
            while True:
                sleep(1)
                try:
                    tabel = self.driver.find_element(self.By.XPATH, '//table[@class="table dataTable table-striped"]').find_element(self.By.TAG_NAME, 'tbody')
                    tr = tabel.find_elements(self.By.TAG_NAME, 'tr')

                    for data in tr:
                        print(data.text.split('\n'))

                    break
                except:
                    pass

    def get_credit(self):
        pass

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

# execute
if __name__ == '__main__':
    mandiri = MandiriLivin(username='shodiq0604', password='Muzaki334', account=1350015688359)
    mandiri.login()
    mandiri.get_debit()
    input("click - Logout!")
    mandiri.logout()
    mandiri.driver_quit()