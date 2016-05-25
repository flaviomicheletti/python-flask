from app import create_app
from app.config import ConfigDev #, ConfigProd

app = create_app(ConfigDev)

if __name__ == "__main__":
    app.run()
