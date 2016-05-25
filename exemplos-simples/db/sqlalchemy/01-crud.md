CRUD com SQLAlchemy
===

Considere o arquivo abaixo como sendo sua aplicação.

```python
#
# Conteúdo do arquivo "yourapplication.py"
#

# coding: utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://user:password@localhost/name-database"
db = SQLAlchemy(app)

class User(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, login, email):
        self.login = login
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.login
```

Para iniciar, acessamos o terminal, importamos sua aplicação e instanciamos 
alguns usuários.

    $ python
    >>> from yourapplication import User
    >>> user1 = User('flavio', 'flavio@email.com.br')
    >>> user2 = User('alexandre', 'alexandre@email.com.br')
    >>> user3 = User('micheletti', 'micheletti@email.com.br')


### Create

    >>> db.session.add(user1)
    >>> db.session.add(user2)
    >>> db.session.add(user3)
    >>> db.session.commit()


### Read

Recuperando todos os registros...

    >>> users = User.query.all()
    >>> for user in users:
    ...  user.login
    ... 
    'flavio'
    'alexandre'
    'micheletti'

Recuperando um registro individualmente...

    >>> user = User.query.get(1)
    >>> user.login
    'flavio'

    >>> user = User.query.get(2)
    >>> user.login
    'alexandre'

    >>> user = User.query.get(3)
    >>> user.login
    'micheletti'


### Update

    >>> user = User.query.get(1)
    >>> user.login = "Flavio"
    >>> db.session.commit()


### Delete

    >>> user = User.query.get(1)
    >>> db.session.delete(user)
    >>> db.session.commit()
