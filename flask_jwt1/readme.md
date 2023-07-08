# flask-jwt-extended

- https://flask-jwt-extended.readthedocs.io/en/stable/

    curl --request POST \
      --url http://localhost:5001/login \
      --header 'content-type: application/json' \
      --data '{"username": "john", "password": "1234"}'


    curl --request GET \
      --url http://localhost:5001/protected \
      --header 'authorization: Bearer <access_token>'

    curl --request GET \
      --url http://localhost:5002/secure-data \
      --header 'authorization: Bearer <access_token>'


# 100% coverage

    coverage run -m unittest discover
    coverage report -m &&  coverage html
