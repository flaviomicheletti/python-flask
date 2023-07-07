from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import postgres_uri

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)