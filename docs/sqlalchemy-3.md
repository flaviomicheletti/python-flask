# SQLAlchemy

## Question

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import postgres_uri

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```

Sometimes I see people using `db = SQLAlchemy(app)` and sometimes I see 
people using it that way `db = SQLAlchemy()`. What would be the difference 
between the two? 

The difference between `db = SQLAlchemy(app)` and `db = SQLAlchemy()` lies in 
how the SQLAlchemy object is instantiated and configured in the Flask 
application. 


## Answer

1. `db = SQLAlchemy(app)`: In this case, an instance of the `SQLAlchemy` 
class is created and initialized with the Flask application object (`app`). 
By passing the `app` object during instantiation, the SQLAlchemy instance is 
directly bound to the Flask application. This means that the Flask 
application and the SQLAlchemy instance share the same configuration and 
context, allowing you to easily access the database within your Flask 
application. 

   ```python
   app = Flask(__name__)
   db = SQLAlchemy(app)
   ```

2. `db = SQLAlchemy()`: Here, an instance of the `SQLAlchemy` class is 
created without passing the Flask application object during instantiation. In 
this case, the SQLAlchemy object is created independently and needs to be 
explicitly initialized with the Flask application later. 

   ```python
   app = Flask(__name__)
   db = SQLAlchemy()
   db.init_app(app)
   ```

   After creating the `SQLAlchemy` object, you call the `init_app()` method and 
   pass the Flask application object (`app`) as an argument. This initializes 
   the SQLAlchemy object with the Flask application, allowing it to access the 
   application's configuration and context. 


In summary, the difference between the two approaches is in the timing of 
initializing the SQLAlchemy object with the Flask application. Using `db = 
SQLAlchemy(app)` directly binds the SQLAlchemy instance to the Flask 
application during instantiation, while `db = SQLAlchemy()` requires an 
explicit call to `db.init_app(app)` to establish the connection between 
SQLAlchemy and Flask. Both approaches achieve the same result, but the first 
one is more concise and convenient.