# flask.g

You may have seen something like this before....

```python
user = getattr(flask.g, 'user', None)
user = flask.g.get('user', None)
```

[flask.g](http://flask.pocoo.org/docs/0.10/api/#flask.g) is a good place to
store global variables. It works within the
[application context](http://flask.pocoo.org/docs/0.10/appcontext/).


### How it works

Let's start Python from the terminal.

    $ python
    >>> from flask import Flask, g

Check if `g` is visible.

    >>> g
    <LocalProxy unbound>

OK, if we assign any value to any variable, we will receive an error 
saying that we are outside the context.

    >>> g.num = 123
    RuntimeError: working outside of application context


So let's create the context.

    >>> app = Flask(__name__)
    >>> with app.app_context():
    ...  print(g)
    ... 
    <flask.g of '__main__'>

We see that `g` points to the correct object.

Now let's test it.

    >>> with app.app_context():
    ...   g.num = 123
    ...   print(g.num)
    ... 
    123


One detail about `app_context()` is that each created context is a 
distinct context, obviously. In other words, we can encounter the 
following error:

    >>> with app.app_context():
    ...   g.num = 123
    ... 
    >>> with app.app_context():
    ...   print(g.num)
    ... 
    AttributeError: '_AppCtxGlobals' object has no attribute 'num'

If we use the `flask.g.get('')` function, we silence the error, 
it simply returns nothing.

    >>> with app.app_context():
    ...   print(g.get('num'))
    ... 


The second parameter of the function can be used as the default 
value if the property does not exist.

    >>> with app.app_context():
    ...   g.get('foo', 100)
    ... 
    100

We have `100` as the response (return) because `foo` does not exist.

Before version 0.10, we used `getattr()`, the forms below are equivalent.

    getattr(g, 'foo', None)
    g.get('foo', None)

Or, with the "full" path...

    getattr(flask.g, 'foo', None)
    flask.g.get('foo', None)

Now, assigning the value to any variable...

```python
foolish = getattr(flask.g, 'foo', None)
foolish = flask.g.get('foo', None)
```