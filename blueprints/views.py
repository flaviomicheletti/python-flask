from flask import Blueprint
from model import User

blueprint = Blueprint('index', __name__)

@blueprint.route('/')
def hello_model():
    user = User.query.filter_by(id=1).first()
    return "Hello user %s!" % user.username