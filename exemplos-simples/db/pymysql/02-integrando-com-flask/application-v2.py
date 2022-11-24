# coding: utf-8
from flask import Flask, g
from flask import render_template
import pymysql

app = Flask(__name__)

def connect_db():
    return pymysql.connect(host='localhost', port=3306, user='', passwd='', db='mysql')

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    cursor = g.db.cursor()

    users_total = cursor.execute('SELECT Host, User FROM user')

    class User():
        pass

    users = []
    for row in cursor:
        user = User()
        user.host  = row[0]
        user.login = row[1]
        users.append(user)

    cursor.close()

    return render_template('index.html', users=users)

