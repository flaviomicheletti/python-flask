import os


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = "alterar"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DATABASE_CONNECT_OPTIONS = {}
    DATABASES = {
        "dev": "sqlite:///dev.db",  # interno e cliente teste
        "prod": "sqlite:///prod.db",  # interno
        "base1": "sqlite:///base1.db",
        "base2": "sqlite:///base2.db",
        "base3": "sqlite:///base3.db",
    }


class ConfigDev(Config):
    CONFIG = "Desenvolvimento"
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    # Visualizar no terminal as execuções das querys
    SQLALCHEMY_ECHO = False
    NOME_DB = "dev"


class ConfigProd(Config):
    CONFIG = "Produção"
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'
    SQLALCHEMY_ECHO = False
    NOME_DB = "prod"
