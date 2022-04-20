# from mimetypes import init
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class DriverChrome:
    def __init__(self):
        print("Driver-Installer..")
        options = Options()
        options.add_argument("--disable-notifications")
        # options.add_argument("--headless")
        # options.add_argument("--window-size=200,400")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=webdriver.ChromeOptions())
        self.By = By
        self.Select = Select