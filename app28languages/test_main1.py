import unittest
from unittest import mock
from app28languages.app import app


class TestApp(unittest.TestCase):
    @mock.patch("app28languages.app.jsonify")
    def test_get_languages(self, mock_jsonify):
        
        client = app.test_client()
        response = client.get("/languages")
        
        self.assertEqual(response.status_code, 200)
        mock_jsonify.assert_called_with([])

"""
The `assert_called_with method` is a testing method used in Python's unittest 
module to check whether a specific function or method has been called with 
the expected arguments.
"""