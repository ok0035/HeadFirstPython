from flask import Flask, session
from webapp.checker import check_logged_in

app = Flask(__name__)
app.secret_key = "What's this"

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'

@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This is page 1.'

@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'This is page 2.'

@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'This is page 3.'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are no logged out.'

@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session.keys() and session['logged_in'] is True:
        return 'You are currently logged in'
    elif 'logged_in' not in session.keys():
        return 'You are NOT logged in'
    else:
        return 'Unknown Error'


if __name__ == '__main__':
    app.run(debug=True)

