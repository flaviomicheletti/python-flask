from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import postgres_uri


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Language(db.Model):
    __tablename__ = 'languages'

    language_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created = db.Column(db.TIMESTAMP, nullable=False)
    last_update = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return f"<Language(language_id={self.language_id}, name='{self.name}', created='{self.created}', last_update='{self.last_update}')>"

with app.app_context():
    # Fetch all rows from the languages table
    all_languages = Language.query.all()

    # Print the retrieved languages
    for language in all_languages:
        print(language.name)

"""
print app.py

English
Spanish
French
German
Italian
"""

