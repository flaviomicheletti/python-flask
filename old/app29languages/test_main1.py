import unittest
from unittest.mock import MagicMock, patch
import psycopg2

from app29languages import app


class TestGetLanguages(unittest.TestCase):

    @patch('psycopg2.connect')
    def test_get_languages(self, mock_conn):
        # mock the cursor object
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, 'English'), (2, 'Italian'), (3, 'Japanese')]

        # mock the cursor method to return the mock cursor object
        mock_conn.return_value.cursor.return_value = mock_cursor

        # call the function to test
        result = app.get_languages()

        # assert that the correct SQL query was executed
        mock_cursor.execute.assert_called_once_with('SELECT * FROM language')

        # assert that the result matches the expected output
        self.assertEqual(result, [(1, 'English'), (2, 'Italian'), (3, 'Japanese')])

