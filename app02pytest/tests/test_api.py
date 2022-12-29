import pytest
from flask import json
from api.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    assert client.get("/").status_code == 200


def test_custom(client):
    assert (
        client.post(
            "/custom",
            data=json.dumps({"foo": True}),
            content_type="application/json",
        ).status_code == 200
    )

    assert (
        client.post(
            "/custom",
            data=json.dumps({"foo": False}),
            content_type="application/json",
        ).status_code == 200
    )

def test_health(client):
    assert client.get("/health").status_code == 200
