import unittest
from unittest.mock import MagicMock, patch
import psycopg2

from app29languages import app


class TestGetLanguages(unittest.TestCase):

    def setUp(self):
        # configure mock database connection
        self.mock_conn = MagicMock(name='psycopg2.connect')
        self.mock_cursor = MagicMock(name='psycopg2.cursor')
        self.mock_conn.cursor.return_value = self.mock_cursor
        self.mock_fetchall = MagicMock(name='cursor.fetchall')
        self.mock_cursor.fetchall.return_value = [('English',), ('Spanish',)]

        # patch the psycopg2.connect method to return the mock connection
        self.patcher = patch('psycopg2.connect', return_value=self.mock_conn)
        self.patcher.start()

    def tearDown(self):
        # stop the patcher
        self.patcher.stop()

    def test_get_languages(self):
        # call the function and assert the result
        result = app.get_languages()
        self.assertEqual(result, [('English',), ('Spanish',)])

        # assert that the mock connection and cursor were called with the correct arguments
        self.mock_conn.cursor.assert_called_once()
        self.mock_cursor.execute.assert_called_once_with('SELECT * FROM language')
        self.mock_cursor.fetchall.assert_called_once()
        self.mock_cursor.close.assert_called_once()
