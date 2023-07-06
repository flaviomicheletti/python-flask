from flask import Flask, jsonify
from .db import get_languages

app = Flask(__name__)


@app.route("/languages", methods=["GET"])
def main():
    return jsonify(get_languages())

# """
# [
#    [
#       1,
#       "English",
#       "Wed, 01 Mar 2023 12:00:00 GMT",
#       "Wed, 01 Mar 2023 12:00:00 GMT"
#    ],
#    [
#       2,
#       "Spanish",
#       "Thu, 02 Mar 2023 12:00:00 GMT",
#       "Thu, 02 Mar 2023 12:00:00 GMT"
#    ],
#    [
#       3,
#       "French",
#       "Fri, 03 Mar 2023 12:00:00 GMT",
#       "Fri, 03 Mar 2023 12:00:00 GMT"
#    ],
#    [
#       4,
#       "German",
#       "Sat, 04 Mar 2023 12:00:00 GMT",
#       "Sat, 04 Mar 2023 12:00:00 GMT"
#    ],
#    [
#       5,
#       "Italian",
#       "Sun, 05 Mar 2023 12:00:00 GMT",
#       "Sun, 05 Mar 2023 12:00:00 GMT"
#    ]
# ]
# """