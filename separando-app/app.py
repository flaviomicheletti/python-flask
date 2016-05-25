from flask import Flask
from extensions import db
from config import ConfigDev # ConfigProd para ambiente de produção

def create_app():
    app = Flask("foo")
    app.config.from_object(ConfigDev)
    db.init_app(app)

    return app
