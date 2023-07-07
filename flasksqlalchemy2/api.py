from flask import jsonify
from main import app
import model


@app.route('/languages', methods=['GET'])
def get_languages():
    all_languages = model.read_all()
    return jsonify(all_languages)