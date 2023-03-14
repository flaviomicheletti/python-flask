# Flask Repos
![image](https://user-images.githubusercontent.com/1257048/204000578-b8185c2f-6df5-4f63-8f26-3265b3cf01a7.png)


Some good examples of using the [Flask framework](https://flask.palletsprojects.com/).


## Enviroment

    cd folder/
    python3 -m venv .venv && . .venv/bin/activate

## Install

    pip install -r requirements.txt
    pip install psycopg2-binary

## Deps

    Flask
    Flask-SQLAlchemy
    itsdangerous
    Jinja2
    MarkupSafe
    SQLAlchemy
    Werkzeug


## Run

    flask --app foo run

http://127.0.0.1:5000


## Tests

    # na pasta raiz
    clear && coverage run -m unittest discover -v
    coverage report -m
    coverage html
