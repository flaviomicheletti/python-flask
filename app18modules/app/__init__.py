from flask import Flask
from app.extensions import db
from app.config import ConfigDev
from users.views import bp_users
from posts.views import bp_posts


def create_app():
    app = Flask("app")  # Nome da pasta que contém este arquivo
    app.config.from_object(ConfigDev)

    db.init_app(app)

    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_posts)
    return None
