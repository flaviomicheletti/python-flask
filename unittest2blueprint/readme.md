# Readme

__test:__

    curl -X GET http://localhost:5000/
    curl -X GET http://localhost:5000/health
    curl -X POST -H "Content-Type: application/json" -d '{"foo": true}' http://localhost:5000/custom
    curl -X POST -H "Content-Type: application/json" -d '{}' http://localhost:5000/custom

__notes:__

    app.register_blueprint(simple_page, url_prefix='/pages')