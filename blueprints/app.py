from flask import Flask
from extensions import db
from config import ConfigDev # ConfigProd para ambiente de produção
from views import bp_index

def create_app():
    app = Flask("foo")
    app.config.from_object(ConfigDev)
    db.init_app(app)
    
    register_blueprints(app)

    return app

def register_blueprints(app):
    app.register_blueprint(bp_index)
    return None