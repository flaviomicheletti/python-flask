import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("mongodb_host")
port = os.getenv("mongodb_port")
database = os.getenv("mongodb_database")


def monogodb_uri():
    username = os.getenv("mongodb_username")
    password = os.getenv("mongodb_password")
    uri = f"mongodb://{username}:{password}@{host}:{port}/"
    # print(uri)
    return uri
