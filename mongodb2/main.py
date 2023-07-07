from flask import Flask, jsonify
from pymongo import MongoClient
from database import db


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_data():
    collection = db['customers']

    # result = []
    # for item in collection.find():
    #     result.append({'name': item['name'], 'address': item['address']})
    # return result

    data = collection.find({}, {'_id': 0, 'name': 1, 'address': 1})
    return jsonify(list(data))
