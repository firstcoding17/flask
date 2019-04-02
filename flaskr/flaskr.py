import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from __future__ import with_statement
from contextlib import closing
from flaskr import init_db
init_db()

DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app=Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)




