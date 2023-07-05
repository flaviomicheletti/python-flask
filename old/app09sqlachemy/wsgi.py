#
#  Model database
#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("foo")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5438/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username


@app.route("/<id>")
def hello_model(id):
    user = Users.query.filter_by(user_id=id).first()
    return "Hello user %s!" % user.name


"""
flask --debug run
"""