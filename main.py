from libmodul.mandiri import Mandiri

# Login
app = Mandiri()
app.login(username="shodiq0604", password="Muzaki334")

# create cookie
app.getcookies()

# get balance
input('Get balance')
bal = app.get_balance()
print(bal)

# get mutasi
input('Get Mutasi')
mut = app.mutasi("1350015688359", "1648746000000", "1649869200000", "D", "")
print(mut)

# Logout
input('Logout.')
app.logout_request()

# Quit-Sel
input('Quit-Sel')
app.driver_quit()