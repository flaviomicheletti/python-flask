# Templates as a Module or Package

For both cases, the content of the `hello.html` file is identical:

```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
```

### Module

File structure:

    templates/
        hello.html
    application.py

Contents of the `application.py` file:

```python
# coding: utf-8
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

### Package

File structure:

    application/
        templates/
            hello.html
        __init__.py