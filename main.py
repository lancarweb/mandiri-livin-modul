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
        while True:
            sleep(1)
            try:
                self.driver.find_element(self.By.XPATH, '//*[text()="{}"]'.format(self.account)).click()
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