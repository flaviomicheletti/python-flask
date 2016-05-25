from flask import Blueprint
from posts.model import Post

bp_posts = Blueprint('posts', __name__)

@bp_posts.route('/posts')
def hello_posts():
    post = Post.query.filter_by(id=1).first()
    return "%s<br><br> %s" % (post.title, post.content)