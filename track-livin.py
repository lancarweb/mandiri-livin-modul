from time import sleep
from libmodul.mandiri import MandiriAuth, MandiriLivin

try:
    while True:
        
        # auth
        mandiri = MandiriAuth()
        mandiri.login(username='shodiq0604', password='Muzaki334')
        mandiri.getcookies()
        mandiri.driver_quit()

        # app
        mandiri_app = MandiriLivin()
        print('\n')
        print(mandiri_app.get_balance())
        sleep(5)
        print('\nLogout')
        mandiri_app.logout_request()

        print('\nwait 15sc')
        sleep(15)
        
except KeyboardInterrupt:
    print('Logout|Auto')
    mandiri_app.logout_request()