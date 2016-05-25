# coding: utf-8
from flask import Flask, g
from flask import render_template
import pymysql

# configuration
DEBUG      = True
SECRET_KEY = 'development key'
DATABASE   = 'mysql'
USERNAME   = ''
PASSWORD   = ''

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return pymysql.connect(
        host='localhost', 
        port=3306, 
        user=app.config['USERNAME'], 
        passwd=app.config['PASSWORD'], 
        db=app.config['DATABASE']
    )

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

    cursor.execute('SELECT Host, User FROM user')

    #
    # List Comprehensions
    #
    users = [dict(host=row[0], login=row[1]) for row in cursor.fetchall()]

    return render_template('index.html', users=users)

if __name__ == "__main__":
    app.run(debug = True)