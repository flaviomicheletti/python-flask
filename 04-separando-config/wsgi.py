from flask import Flask
from model import User
from extensions import db
from config import ConfigDev  

app = Flask("foo")
app.config.from_object(ConfigDev)
db.init_app(app)


@app.route("/")
def hello_model():
    user = User.query.filter_by(id=1).first()
    return "Hello user %s!" % user.username
