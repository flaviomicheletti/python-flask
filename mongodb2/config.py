import os
from dotenv import load_dotenv

load_dotenv()

database = os.getenv("mongodb_database")

def monogodb_uri():
    host = os.getenv("mongodb_host")
    port = os.getenv("mongodb_port")
    username = os.getenv("mongodb_username")
    password = os.getenv("mongodb_password")
    uri = f"mongodb://{username}:{password}@{host}:{port}/"
    # print(uri)
    return uri

