from flask import Flask
from custom import views as custom_views
from health import views as health_views


app = Flask(__name__)
app.register_blueprint(custom_views.router)
app.register_blueprint(health_views.router)
