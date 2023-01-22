from flask import Flask
from extensions import db
from config import ConfigDev
from views import blueprint


def create_app():
    app = Flask("foo")
    app.config.from_object(ConfigDev)
    db.init_app(app)

    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(blueprint)
    return None
