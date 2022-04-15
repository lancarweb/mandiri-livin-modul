# from crypt import methods
from flask import Flask, request, jsonify
from libmodul.mandiri import MandiriAuth, MandiriLivin

app = Flask(__name__)

@app.route('/')
def home():
    return 'mandiri v.0'

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # auth
        mandiri = MandiriAuth()
        mandiri.login(username=username, password=password)
        
        # create cookies
        mandiri.getcookies()

        # Quit|selenium
        mandiri.driver_quit()

        return 'auth post sukses'

    else:
        return 'err. get login'

@app.route('/getbalance')
def get_balance():
    mandiri = MandiriLivin()
    balance = mandiri.get_balance()
    return balance

@app.route('/mutasi', methods=['GET', 'POST'])
def mutasi():
    if request.method == 'POST':
        number_account = request.form['account']
        fromdate = request.form['fromdate']
        todate = request.form['todate']
        typ = request.form['type']
        keywd = request.form['keyword']

        mandiri = MandiriLivin()
        mutasi_ = mandiri.mutasi(number_account, fromdate, todate, typ, keywd)

        return mutasi_
        
    else:
        return 'err. get mutasi'

@app.route('/logout')
def logout():
    mandiri = MandiriLivin()
    mandiri.logout_request()
    
    return 'logout'

# if __name__ == '__main__':
#     app.run(debug=True)