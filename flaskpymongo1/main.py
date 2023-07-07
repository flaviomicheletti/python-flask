from flask import Flask, jsonify
from flask_pymongo import PyMongo
from config import monogodb_uri, database


app = Flask(__name__)
app.config["MONGO_URI"] = monogodb_uri()
pymongo = PyMongo(app)

client = pymongo.cx
db = client[database]

collection = db['customers']
print(collection)

for doc in collection.find():
    print(doc)

""""
{'_id': ObjectId('64a83e075cea11a07b49b910'), 'name': 'John', 'address': 'Highway 37'}
{'_id': ObjectId('64a84c1c58e864522a9eec87'), 'name': 'John', 'address': 'Highway 37'}
"""
