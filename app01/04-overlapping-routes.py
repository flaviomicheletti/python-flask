# coding: utf-8
from flask import Flask

app = Flask(__name__)

#
# /, /foo e /dummy they point to 'home'
#
@app.route("/")
@app.route("/foo")
@app.route("/dummy")
def home():
    return "home"


if __name__ == "__main__":
    app.run(debug=True)
