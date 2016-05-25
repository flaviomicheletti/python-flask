Templates como módulo ou pacote
===


Para ambos os casos ao conteúdo do arquivo `hello.html` é idêntico:

```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
```



### Módulo

Estrutura de arquivos...

    templates/
        hello.html
    application.py

Conteúdo do arquivo `application.py`:

```python
# coding: utf-8
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.debug = True
    app.run()
```



### Pacote

Estrutura de arquivos...

    application/
        templates/
            hello.html
        __init__.py


