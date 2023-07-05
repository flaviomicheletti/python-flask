""" does not cover rows 27 and 28 """

import json
import unittest
from unittest.mock import patch, MagicMock
from app26languages.app import app


class TestApp(unittest.TestCase):
    def test_get_languages(self):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            (1, "English"),
            (2, "Italian"),
            (3, "Japanese"),
        ]

        # mock the cursor method to return the mock cursor object
        mock_conn = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor

        # Replace the psycopg2.connect() function with a function that returns the mock connection object
        with patch("psycopg2.connect", return_value=mock_conn):
            # Create a test client for the Flask application
            client = app.test_client()

            # Send a GET request to the /languages endpoint and retrieve the response
            response = client.get("/languages")

            # Convert the response data from JSON to a Python object
            data = json.loads(response.data)

            # Test the content of the response data
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data, [])
            assert len(data) == 0  # No data since mock connection
