import psycopg2

# configuration
DEBUG = True
HOST = "localhost"
DATABASE = "dvdrental"
USERNAME = "myuser"
PASSWORD = "mypassword"


# set up the database connection
def getConn():
    return psycopg2.connect(
        dbname=DATABASE,
        user=USERNAME,
        password=PASSWORD,
        host=HOST,
        port=5432,
    )


def get_languages():
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM language")
    languages = cursor.fetchall()
    cursor.close()
    return languages
