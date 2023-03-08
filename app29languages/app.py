from flask import Flask, jsonify
import psycopg2

# configuration
DEBUG = True
HOST = "localhost"
DATABASE = "dvdrental"
USERNAME = "myuser"
PASSWORD = "mypassword"


app = Flask(__name__)

# set up the database connection
conn = psycopg2.connect(
    dbname=DATABASE,
    user=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=5432,
)


@app.route("/languages", methods=["GET"])
def get_languages():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM language")
    languages = cursor.fetchall()
    cursor.close()
    return jsonify(languages)


if __name__ == "__main__":
    app.run()


# if __name__ == "__main__":
#     app.debug = DEBUG
#     app.run()
