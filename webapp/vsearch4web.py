from flask import Flask, render_template, request, escape
from vsearch import search4letters
from webapp.DBcm import UseDatabase

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
    phrase = request.form['phrase']
    letters = request.form['letters']

    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results, )


def log_request(req: 'flask_request', res: str) -> None:

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log (phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL,
                       (req.form['phrase'],
                        req.form['letters'],
                        req.remote_addr,
                        req.user_agent.browser,
                        res, ))

    # _SQL = """select * from log"""

    # cursor.execute(_SQL)

    # for row in cursor.fetchall():
    #     print(row)

    # cursor.close()
    # conn.close()

    # with open('vsearch.log', 'a') as log:
    #     print(req.form, req.remote_addr, req.user_agent, req, res, file=log, sep='|')

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title = 'Welcome to search4letters on the web!')

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        
    titles = ('Phrase', 'Letters', 'Remote_addr', 'user_agent', 'Results')

    # with open('vsearch.log') as log:
    #     for line in log:
    #         contents.append([])
    #         splitList = line.split('|')
    #         for item in splitList:
    #             contents[-1].append(escape(item))

    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
