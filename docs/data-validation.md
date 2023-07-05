# data-validation

When I use Fastapi the most common way to validate and verify data is using 
the Pydantic lib. What would be the most common way to validate data when I 
use Flask? 

When using Flask, one of the most common ways to validate and verify data is 
to utilize the Flask-RESTful extension, which provides tools for building 
APIs with Flask. Flask-RESTful includes support for request parsing and input 
validation through its request parsing module, which is similar to Pydantic 
but specifically designed for Flask. 

To use request parsing and input validation with Flask-RESTful, you would 
typically follow these steps:

1. Install Flask-RESTful by running `pip install flask-restful`.

2. Create a Flask application and initialize Flask-RESTful:

   ```python
   from flask import Flask
   from flask_restful import Api

   app = Flask(__name__)
   api = Api(app)
   ```

3. Define a resource that handles the incoming requests and utilizes request parsing:

   ```python
   from flask_restful import Resource, reqparse

   class MyResource(Resource):
       def __init__(self):
           self.parser = reqparse.RequestParser()
           self.parser.add_argument('name', type=str, required=True)
           self.parser.add_argument('age', type=int, required=True)

       def post(self):
           args = self.parser.parse_args()
           name = args['name']
           age = args['age']
           # Process and validate the input data
           # ...

   api.add_resource(MyResource, '/my-endpoint')
   ```

    In this example, the `reqparse.RequestParser` is used to define the expected 
    arguments (`name` and `age`) and their types. By default, these arguments are 
    required, but you can modify that behavior using the `required` parameter.

4. Run the Flask application:

   ```python
   if __name__ == '__main__':
       app.run()
   ```

With this setup, when you make a POST request to the `/my-endpoint` URL with 
the required `name` and `age` parameters, Flask-RESTful will automatically 
parse and validate the incoming data according to the defined rules. 

Flask-RESTful provides many other features and capabilities beyond request 
parsing and validation, making it a powerful extension for building APIs with 
Flask. 



