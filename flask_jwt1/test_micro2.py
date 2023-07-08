import unittest
import json


class Micro2(unittest.TestCase):
    def setUp(self):
        from micro1 import app
        from micro2 import app as secure_app

        self.app = app.test_client()
        self.secure_app = secure_app.test_client()

    def test_secure_data(self):
        payload = {"username": "john", "password": "1234"}
        response = self.app.post(
            "/login", data=json.dumps(payload), content_type="application/json"
        )
        token = response.json["access_token"]
        headers = {"Authorization": "Bearer " + token}
        response = self.secure_app.get("/secure-data", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json,
            {
                "message": "This is sensitive data that requires authentication.",
                "secret": "shhh...",
            },
        )
