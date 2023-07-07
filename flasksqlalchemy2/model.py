from main import db

class Language(db.Model):
    __tablename__ = 'languages'

    language_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created = db.Column(db.TIMESTAMP, nullable=False)
    last_update = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self):
        return f"<Language(language_id={self.language_id}, name='{self.name}', created='{self.created}', last_update='{self.last_update}')>"


def read_all():
    all_languages = Language.query.all()
    languages = []
    for language in all_languages:
        languages.append({
            'language_id': language.language_id,
            'name': language.name,
            'created': language.created,
            'last_update': language.last_update
        })
    return languages