import pymongo
from config import monogodb_uri, database


# create a MongoClient object
client = pymongo.MongoClient(monogodb_uri())
# from config import host, port
# client = pymongo.MongoClient(host, port)

# create a database object
db = client[database]

# create a collection object
col = db["customers"]

# insert a document
doc = {"name": "John", "address": "Highway 37"}
x = col.insert_one(doc)

# print the inserted document's id
print(x.inserted_id)
