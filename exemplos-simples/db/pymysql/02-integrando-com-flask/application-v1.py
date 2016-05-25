# coding: utf-8
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    import pymysql
    connection = pymysql.connect(host='localhost', port=3306, user='', passwd='', db='mysql')

    cursor = connection.cursor()

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
    connection.close()

    return render_template('index.html', users=users)

if __name__ == "__main__":
    app.run(debug = True)