CRUD
===


    $ python
    >>> from flask import Flask
    >>> import pymysql
    >>> connection = pymysql.connect(host='localhost', port=3306, user='', passwd='', db='')
    >>> cursor = connection.cursor()

Limpando a base com `truncate table, não foi preciso aplicar o "commit":

    >>> cursor.execute("TRUNCATE TABLE user")
    0


__Create (insert):__

    >>> cursor.execute("INSERT INTO user VALUES(%s, %s, %s)", (1, 'flavio', 'flavio@email'))
    1
    >>> cursor.execute("INSERT INTO user VALUES(%s, %s, %s)", (2, 'alexandre', 'alexandre@email'))
    1
    >>> cursor.execute("INSERT INTO user VALUES(%s, %s, %s)", (3, 'micheletti', 'micheletti@email'))
    1
    >>> connection.commit()


__Read (select):__


    >>> cursor.execute("SELECT * FROM user")
    3
    >>> for row in cursor.fetchall():
    ...   row
    ... 
    (1, 'flavio', 'flavio@email.com.br')
    (2, 'alexandre', 'alexandre@email.com.br')
    (3, 'micheletti', 'micheletti@email.com.br')


__Update:__

>>> cursor.execute("UPDATE user SET email=%s  WHERE id=%s", ('flavio@email.com.br', 1))
1
>>> cursor.execute("UPDATE user SET email=%s  WHERE id=%s", ('alexandre@email.com.br', 2))
1
>>> cursor.execute("UPDATE user SET email=%s  WHERE id=%s", ('micheletti@email.com.br', 3))
1
>>> connection.commit()



__Delete:__

>>> cursor.execute("DELETE FROM user WHERE id=%s", (1))
1
>>> cursor.execute("DELETE FROM user WHERE id=%s", (2))
1
>>> cursor.execute("DELETE FROM user WHERE id=%s", (3))
1
>>> connection.commit()
