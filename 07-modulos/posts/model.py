from app.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text())

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return "<Post %r>" % self.title
