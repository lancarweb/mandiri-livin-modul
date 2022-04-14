import requests
import json

class Livin:
    def __init__(self, cookies):
        self.url_mutasi = "https://ibank.bankmandiri.co.id/retail3/secure/pcash/retail/account/portfolio/searchTransaction" # mutasi
        self.url_balance = "https://ibank.bankmandiri.co.id/retail3/secure/pcash/retail/account/portfolio/getBalance/1350015688359" # get|balance
        self.url_logout = "https://ibank.bankmandiri.co.id/retail3/loginfo/logout"

        #  Cookies
        Cookie = f'{cookies}'

        self.payload = ""
        self.headers = {
            "cookie": "DC1=SVRC",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Cookie": f"{Cookie}",
            "Host": "ibank.bankmandiri.co.id",
            "Referer": "https://ibank.bankmandiri.co.id/retail3/secure/pcash/retail/account/portfolio/skeleton",
            "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "content-type": "multipart/form-data"
        }

        # session
        self.ses = requests.Session()

    def livin_balance(self):
        # GET|BALANCE
        response_getbalance = self.ses.request("GET", self.url_balance, data=self.payload, headers=self.headers)
        accountBalance = (json.loads(response_getbalance.text)["accountBalance"])
        return (accountBalance)

    def livin_mutasi(self, accountNo, fromDate, toDate, transactionType, keyWord):
        
        # GET|BALANCE
        response_getbalance = self.ses.request("GET", self.url_balance, data=self.payload, headers=self.headers)
        accountBalance = (json.loads(response_getbalance.text)["accountBalance"])

        # QueryString
        # accountNo = '1350015688359'
        availableBalance = 'IDR {}'.format(accountBalance)
        # fromDate = '1648746000000'
        # toDate = '1649869200000'
        # transactionType = 'D' # D|C|optional
        # keyWord = '' # keyword(str)|optional

        # var|query
        querystring = {"":"","accountNo":f"{accountNo}","availableBalance":f"{availableBalance}","searchCasaBy":"PERIOD","fromDate":f"{fromDate}","toDate":f"{toDate}","transactionTypeCode":"S","transactionType":f"{transactionType}","keyWord":f"{keyWord}","_":"1649947221497"}

        # GET|MUTASI
        response_mutasi = self.ses.request("GET", self.url_mutasi, data=self.payload, headers=self.headers, params=querystring)

        return (json.loads(response_mutasi.text))

    def livin_logout(self):
        self.ses.request("GET", self.url_logout, data=self.payload, headers=self.headers)