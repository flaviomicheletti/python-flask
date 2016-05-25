from flask import Flask
from model import User
from extensions import db

app = Flask("foo")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def hello_model():
    user = User.query.filter_by(id=1).first()
    return "Hello user %s!" % user.username

if __name__ == "__main__":
    app.run(debug=True)
