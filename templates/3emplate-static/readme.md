# Static files

Considering the following file structure...

    myapp/
        static/
            style.min.css
        templates/
            index.html
        application.py

We have 2 HTML files...


1) __Hard-coded__

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


2) __Using `url_for`__

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