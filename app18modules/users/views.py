from flask import Blueprint, url_for
from users.model import User

bp_users = Blueprint("users", __name__)


@bp_users.route("/")
def hello_model():
    user = User.query.filter_by(id=1).first()
    return "Hello user %s!<br><a href='%s'>posts</a>" % (
        user.username,
        url_for("posts.hello_posts"),
    )
