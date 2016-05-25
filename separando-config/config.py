import os

class Config(object):
    BASE_DIR   = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = "alterar"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DATABASE_CONNECT_OPTIONS = {}

class ConfigDev(Config):
    CONFIG = "Desenvolvimento"
    DEBUG  = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    
class ConfigProd(Config):
    CONFIG = "Produção"
    DEBUG  = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'
