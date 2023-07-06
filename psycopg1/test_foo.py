import unittest
# from foo import app
from foo.main import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_languages(self):
        response1 = self.app.get(
            "/languages",
            content_type="application/json",
        )
        self.assertEqual(response1.status_code, 200)

