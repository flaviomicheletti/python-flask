from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# configuration
DEBUG = True
HOST = "localhost"
DATABASE = "dvdrental"
USERNAME = "myuser"
PASSWORD = "mypassword"


@app.route("/languages", methods=["GET"])
def get_languages():
    conn = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USERNAME,
        password=PASSWORD,
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM public.language")
    rows = cur.fetchall()
    languages = []
    for row in rows:
        language = {"language_id": row[0], "name": row[1], "last_update": row[2]}
        languages.append(language)
    conn.close()
    return jsonify(languages)


# if __name__ == "__main__":
#     app.debug = DEBUG
#     app.run()
