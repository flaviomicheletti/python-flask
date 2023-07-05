from flask import Flask, Response, jsonify, request


app = Flask(__name__)


@app.route("/")
def index():
    return Response("Hello, world!", status=200)


@app.route("/custom", methods=["POST"])
def custom():
    payload = request.get_json()

    if payload.get("foo") is True:
        output = {"message": "Hello!"}
    else:
        output = {"message": "..."}

    return jsonify(output)


@app.route("/health")
def health():
    return Response("OK", status=200)
