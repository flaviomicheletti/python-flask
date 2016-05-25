pymysql
===

Experimentando [pymysql](https://github.com/PyMySQL/PyMySQL) no terminal.

Você deve ter o __pymysql__ devidamente instalado `pip install pymysql`.


Iniciamos o Python e importamos a biblioteca.
    $ python
    >>> import pymysql

Conectamos com o banco de dados através da função `connect()`.

    >>> connection = pymysql.connect(host='localhost', port=3306, user='', passwd='', db='mysql')
    >>> type(connection)
    <class 'pymysql.connections.Connection'>

Obtemos o cursor.

    >>> cursor = connection.cursor()
    >>> type(cursor)
    <class 'pymysql.cursors.Cursor'>

Executamos um SQL.

    >>> users_total = cursor.execute('SELECT Host, User FROM user')

A função `execute()` retorna um inteiro com o total de registros encontrados.

    >>> type(users_total)
    <class 'int'>
    >>> users_total
    6

Também temos a propriedade `rowcount` com o mesmo valor.

    >>> cursor.rowcount == users_total
    True

Avançando com o cursor, podemos ver o resultado

    >>> for row in cursor:
    ...   row
    ... 
    """ mostra os resultados """

Detalhe: Se quisermos percorrer novamente a consulta devemos executá-la, faz
sentido pois havíamos avançado com o curso e agora ele está no fim do arquivo.

    >>> users_total = cursor.execute('SELECT Host, User FROM user')
    >>> for row in cursor:
    ...   type(row)
    ... 
    <class 'tuple'>
    <class 'tuple'>
    <class 'tuple'>
    <class 'tuple'>
    <class 'tuple'>
    <class 'tuple'>
