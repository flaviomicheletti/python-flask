import unittest
import json


class Micro1(unittest.TestCase):
    def setUp(self):
        from micro1 import app

        self.app = app.test_client()

    def test_login_success(self):
        payload = {"username": "john", "password": "1234"}
        response = self.app.post(
            "/login", data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue("access_token" in response.json)

    def test_login_failure(self):
        payload = {"username": "john", "password": "wrong-password"}
        response = self.app.post(
            "/login", data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.json, {"message": "Invalid username or password"})

    def test_protected(self):
        payload = {"username": "john", "password": "1234"}
        response = self.app.post(
            "/login", data=json.dumps(payload), content_type="application/json"
        )
        token = response.json["access_token"]
        headers = {"Authorization": "Bearer " + token}
        response = self.app.get("/protected", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Access granted"})
