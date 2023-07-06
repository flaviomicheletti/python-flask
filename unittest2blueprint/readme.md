# Readme

__run:__

    flask --app main run

__run tests:__

    python -m unittest discover -v

__coverage:__

    coverage run --source=./ -m unittest discover
    coverage report -m && coverage html

__test:__

    curl -X GET http://localhost:5000/
    curl -X GET http://localhost:5000/health
    curl -X POST -H "Content-Type: application/json" -d '{"foo": true}' http://localhost:5000/custom
    curl -X POST -H "Content-Type: application/json" -d '{}' http://localhost:5000/custom

__notes:__

    app.register_blueprint(simple_page, url_prefix='/pages')