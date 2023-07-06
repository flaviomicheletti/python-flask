from flask import Blueprint, Response

router = Blueprint("health", __name__)


@router.route("/health")
def health():
    return Response("OK", status=200)
