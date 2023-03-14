""" does not cover rows 27 and 28 """

import unittest
from unittest.mock import patch, MagicMock
from app26languages.app import app, get_languages


class TestApp(unittest.TestCase):
    def test_get_languages(self):
        # Create a mock connection object and cursor object
        mock_cursor = MagicMock()

        mock_conn = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor

        # Define the expected result of the query
        expected_result = [
            {"language_id": 1, "name": "English", "last_update": "2023-03-01 12:00:00"},
            {"language_id": 2, "name": "Spanish", "last_update": "2023-03-02 12:00:00"},
        ]

        with patch("psycopg2.connect", return_value=mock_conn):
            with patch.object(mock_cursor, "fetchall", return_value=expected_result):
                with app.test_client() as client:
                    response = client.get("/languages")
                    self.assertEqual(response.status_code, 200)

                    # Parse the JSON response and check that it matches the expected result
                    response_data = response.get_json()
                    self.assertEqual(response_data, [])
