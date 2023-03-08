import unittest
from unittest.mock import patch
from app28languages.app import app


class TestApp(unittest.TestCase):
    @patch("app28languages.app.jsonify")
    def test_get_languages(self, mock_jsonify):
        mock_jsonify.return_value = {}
        
        client = app.test_client()
        response = client.get("/languages")
        
        self.assertEqual(response.status_code, 200)
        mock_jsonify.assert_called_once()
