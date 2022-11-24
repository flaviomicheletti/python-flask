from flask import Flask

app = Flask("foo")


@app.route("/")
def hello():
    return "Hello World!"


"""

flask --app foo run
http://127.0.0.1:5000

"""
