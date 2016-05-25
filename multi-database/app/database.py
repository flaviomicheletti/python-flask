from app.extensions import app, db

def connect_db(nome_db):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASES'][nome_db]
    db.make_connector(app)
    print("connect_db()", db.engine)