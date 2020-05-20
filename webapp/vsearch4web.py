from flask import Flask, render_template, request, escape, copy_current_request_context
from vsearch import search4letters
from webapp.DBcm import UseDatabase, DBConnectionError, CredentialsError, SQLError
from time import sleep
from threading import Thread

import mysql.connector

app = Flask(__name__)
app.config['dbconfig'] = {
        'host': '127.0.0.1',
        'user': 'vsearch',
        'password': '',
        'database': 'vsearchlogDB',
}


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':

    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        sleep(15)
        try:
            with UseDatabase(app.config['dbconfig']) as cursor:
                _SQL = """insert into log (phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s, %s)"""
                cursor.execute(_SQL,
                               (req.form['phrase'],
                                req.form['letters'],
                                req.remote_addr,
                                req.user_agent.browser,
                                res,))

        except DBConnectionError as err1:
            print('Is your database switched on? Error: ', str(err1))
        except CredentialsError as err1:
            print('User-id/Password issues. Error: ', str(err1))
        except SQLError as err1:
            print('Is your query correct? Error: ', str(err1))

        except Exception as err1:
            print('Something went wrong: ', str(err1))

    phrase = request.form['phrase']
    letters = request.form['letters']

    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))

    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('**** Logging failed with this error:', str(err))

    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title = 'Welcome to search4letters on the web!')

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()

        titles = ('Phrase', 'Letters', 'Remote_addr', 'user_agent', 'Results')

        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents, )

    except DBConnectionError as err:
        print('Is your database switched on? Error: ', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error: ', str(err))
    except SQLError as err:
        print('Is your query correct? Error: ', str(err))
    except Exception as err:
        print('Something went wrong: ', str(err))

    return 'Error'


if __name__ == '__main__':
    app.run(debug=True)
