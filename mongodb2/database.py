from pymongo import MongoClient
from config import monogodb_uri, database


client = MongoClient(monogodb_uri())
db = client[str(database)]
