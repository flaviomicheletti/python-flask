from flask import Flask, jsonify
from flask_pymongo import PyMongo
from config import monogodb_uri, database


app = Flask(__name__)
app.config["MONGO_URI"] = monogodb_uri()
pymongo = PyMongo(app)

client = pymongo.cx
db = client[database]


@app.route('/', methods=['GET'])
def get_data():
    collection = db['customers']

    data = collection.find({}, {'_id': 0, 'name': 1, 'address': 1})
    return jsonify(list(data))


