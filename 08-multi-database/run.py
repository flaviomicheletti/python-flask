from app import create_app
from app.config import ConfigDev

app = create_app(ConfigDev)
