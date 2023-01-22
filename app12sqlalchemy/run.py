from model import User
from app import create_app

app = create_app()

@app.route("/")
def hello_model():
    user = User.query.filter_by(id=1).first()
    return "Hello user %s!" % user.username


