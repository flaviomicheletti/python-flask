from flask import Blueprint, Response, jsonify, request

router= Blueprint("custom", __name__)


@router.route("/")
def index():
    return Response("Hello, world!", status=200)


@router.route("/custom", methods=["POST"])
def custom():
    payload = request.get_json()

    if payload.get("foo") is True:
        output = {"message": "Hello!"}
    else:
        output = {"message": "..."}

    return jsonify(output)

