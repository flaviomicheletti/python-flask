from flask import Blueprint
from posts.model import Post
from app.database import connect_db
from app.extensions import db

bp_posts = Blueprint("posts", __name__)


@bp_posts.route("/<string:nome_db>")
def hello_posts(nome_db):
    connect_db(nome_db)
    post = Post.query.filter_by(id=1).first()
    print("posts<" + nome_db + ">: ", db.engine)
    return "%s<br><br> %s" % (post.title, post.content)
