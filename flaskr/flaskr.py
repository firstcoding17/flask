from __future__ import with_statement
from contextlib import closing

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()



import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app=Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)






if __name__ == '__main__':
    app.run()


import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app=Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

from flaskr import init_db
init_db()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()


if __name__ == '__main__':
    app.run()




