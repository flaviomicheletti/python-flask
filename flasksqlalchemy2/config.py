import os
from dotenv import load_dotenv

load_dotenv()

def postgres_uri():
    host = os.getenv("host")
    port = os.getenv("port")
    database = os.getenv("database")
    username = os.getenv("username")
    password = os.getenv("password")
    uri = f"postgresql://{username}:{password}@{host}:{port}/{database}"
    print(uri)
    return uri
