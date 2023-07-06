# SQLAlchemy

To use [SQLAlchemy](http://www.sqlalchemy.org/) in your Flask project, you 
have to choose between the pure installation (plan) and using SQLAlchemy as 
an extension (plugin).

Pure installation:

    pip install sqlalchemy

Installation as an extension:

    pip install Flask-SQLAlchemy

The examples in this repository are based on the second option (installation 
as an extension). 

Additionally, depending on your choice of database, you must have the 
corresponding database driver properly installed. 

For MySQL users, you have two driver options: MySQLdb and pymysql.

Create a file named `yourapplication.py` with the following content:

```python
#
# Contents of the file "yourapplication.py"
#

# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "see options below"
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

The value of `SQLALCHEMY_DATABASE_URI` will depend on your database choice.

1. sqlite:

    `"sqlite:////tmp/test.db"`

2. MySQL with MySQLdb driver:

    `"mysql://user:password@localhost/name-database"`

3. MySQL with pymysql driver:

    `"mysql+pymysql://user:password@localhost/name-database"`

4. PostgreSQL:

    `"postgresql://user:password@localhost/name-database"`

Once you have defined the database, run Python in the terminal.

Make sure to run Python from the same folder where you created the
`yourapplication.py` file.

    $ ls
    yourapplication.py
    $ python

Create the database and generate the schema by executing `create_all()`.

    >>> from yourapplication import db
    >>> db.create_all()

For MySQL, the following table will be created:

    CREATE TABLE IF NOT EXISTS `user` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `login` varchar(80) DEFAULT NULL,
      `email` varchar(120) DEFAULT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `email` (`email`),
      UNIQUE KEY `login` (`login`)
    ) ENGINE=InnoDB DEFAULT;


## Documentation

- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.0/)
- [SQLAlchemy in Flask](http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/)
- [SQLAlchemy 0.9 Documentation](http://docs.sqlalchemy.org/en/rel_0_9/)