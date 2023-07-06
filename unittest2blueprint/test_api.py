import unittest
from flask import json
from main import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_custom(self):
        response1 = self.app.post(
            "/custom",
            data=json.dumps({"foo": True}),
            content_type="application/json",
        )
        self.assertEqual(response1.status_code, 200)

        response2 = self.app.post(
            "/custom",
            data=json.dumps({"foo": False}),
            content_type="application/json",
        )
        self.assertEqual(response2.status_code, 200)

    def test_health(self):
        response = self.app.get("/health")
        self.assertEqual(response.status_code, 200)

