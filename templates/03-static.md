Static files
===

Considerando a seguinte estrutura de arquivos...

    myapp/
        static/
            style.min.css
        template/
            index.html
        application.py

Temos 2 HTML's ...


1) __hard code__

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <title></title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="/static/style.min.css">
    </head>
    <body></body>
</html>
```


2) __url_for__

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <title></title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="{{ url_for('static', filename='style.min.css') }}">
    </head>
    <body></body>
</html>
```

