from app.extensions import app, db
from users.views import bp_users
from posts.views import bp_posts
from app.database import connect_db


def create_app(config):
    app.config.from_object(config)

    db.init_app(app)

    register_blueprints(app)

    @app.before_request
    def init_db():
        connect_db(app.config["NOME_DB"])
        print("before_request: ", db.engine)

    return app


def register_blueprints(app):
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_posts, url_prefix="/posts")
    return None
