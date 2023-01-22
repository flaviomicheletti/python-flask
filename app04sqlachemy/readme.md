SQLAlchemy
===

Para utilizar o [SQLAlchemy](http://www.sqlalchemy.org/) em seu projeto Flask 
você terá que optar entre a instalação pura (plan) e utilização do SQLAlchemy 
como extension (plugin).

Instalação pura...

    pip install slqalchemy

Instalação como extensão...

    pip install Flask-SQLAlchemy

Os exemplos deste repositório se limita a segunda opção (instalação como extensão).

Além disso, dependendo de sua escolha como bando de dados, você também deve ter 
o driver de seu banco devidamente instalado.

Para usuários do MySQL você terá duas opções de divers: MySQLdb e pymysql.

Crie um arquivo denominado `yourapplication.py` com o seguinte conteúdo...

```python
#
# Conteúdo do arquivo "yourapplication.py"
#

# coding: utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "veja opções adiante"
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


O valor de `SQLALCHEMY_DATABASE_URI` irá depender de seu banco de dados.

1. sqlite: 

    `"sqlite:////tmp/test.db"`

2. MySQL com dirver MySQLdb:

    `"mysql://user:password@localhost/name-database"`

3. MySQL com dirver pymysql:

    `"mysql+pymysql://user:password@localhost/name-database"`

4. PostgreSQL:

    `"postgresql://user:password@localhost/name-database"`


Definido o banco de dados, acione o Python pelo terminal.

Obviamente, o Python deve ser acionado estando-se na mesma pasta onde criamos o
arquivo `yourapplication.py`.

    $ ls
    yourapplication.py    
    $ Python

Crie a base de dados e gere o "schema" executando `create_all()`.

    >>> from yourapplication import db
    >>> db.create_all()


No MySQL foi criado a seguinte tabela...

    CREATE TABLE IF NOT EXISTS `user` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `login` varchar(80) DEFAULT NULL,
      `email` varchar(120) DEFAULT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `email` (`email`),
      UNIQUE KEY `login` (`login`)
    ) ENGINE=InnoDB DEFAULT;



Documentação
---

- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.0/)
- [SQLAlchemy in Flask](http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/)
- [SQLAlchemy 0.9 Documentation](http://docs.sqlalchemy.org/en/rel_0_9/)