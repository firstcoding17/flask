"""Flask Login Example and instargram fallowing find"""

from flask import Flask,url_for,render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
import  UserDB

app = Flask(__name__)
app.config['SQLCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    """create user table"""
    id = db.Column(db.Integer,prmary_key=True)
    username = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))
    email =db.Column(db.String(100),unique = True)
    money = db.Column(db.integer,)
    def __init__(self,username,password):
