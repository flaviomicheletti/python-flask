from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


@app.route("/languages", methods=["GET"])
def get_languages():
    # cursor = conn.cursor()
    # cursor.close()
    return jsonify([{}, {}])


# if __name__ == "__main__":
#     app.run()