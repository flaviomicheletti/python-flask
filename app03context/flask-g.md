flask.g
===


Você já deve ter visto algo parecido com isto....

```python
user = getattr(flask.g, 'user', None)
user = flask.g.get('user', None)
```

[flask.g](http://flask.pocoo.org/docs/0.10/api/#flask.g) é um bom lugar para se
colocar variáveis globais.  Ela funciona dentro do 
[contexto da aplicação](http://flask.pocoo.org/docs/0.10/appcontext/).



### Como funciona

Iniciamos o Python pelo terminal.

    $ python
    >>> from flask import Flask, g

Checamos se `g` está visível.

    >>> g
    <LocalProxy unbound>

OK, se atribuírmos um valor qualquer a uma variável qualquer receberemos um
erro dizendo que estamos fora do contexto.

    >>> g.num = 123
    RuntimeError: working outside of application context


Então vamos criar o contexto.

    >>> app = Flask(__name__)
    >>> with app.app_context():
    ...  print(g)
    ... 
    <flask.g of '__main__'>

Percebemos que `g` aponta para o objeto correto.

Agora, vamos testar.

    >>> with app.app_context():
    ...   g.num = 123
    ...   print(g.num)
    ... 
    123


Um detalhe sobre `app_context()` é que cada contexto criado é um contexto distinto,
obviamente. Em outras palavras, podemos cair no seguinte erro:

    >>> with app.app_context():
    ...   g.num = 123
    ... 
    >>> with app.app_context():
    ...   print(g.num)
    ... 
    AttributeError: '_AppCtxGlobals' object has no attribute 'num'

Se utilizarmos a função `flask.g.get('')` silenciamos o erro, ela simplesmente
não retorna nada.

    >>> with app.app_context():
    ...   print(g.get('num'))
    ... 


O segundo parâmetro da função pode ser utilizado como valor padrão no caso da
propriedade não existir.

    >>> with app.app_context():
    ...   g.get('foo', 100)
    ... 
    100

Temos `100` como resposta (retorno) porque `foo` não existe.

Antes da versão 0.10 utilizávamos `getattr()`, as formas abaixo são equivalentes.

    getattr(g, 'foo', None)
    g.get('foo', None)

Ou, com o camiho "completo"...

    getattr(flask.g, 'foo', None)
    flask.g.get('foo', None)

Agora, atribuindo o valor a uma variável qualquer...

```python
foolish = getattr(flask.g, 'foo', None)
foolish = flask.g.get('foo', None)
```