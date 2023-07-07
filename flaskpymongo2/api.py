from flask import jsonify
from main import app, db


@app.route('/', methods=['GET'])
def get_languages():
    return jsonify({'languages': 'languages'})
