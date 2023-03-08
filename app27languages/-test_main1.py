import json
import unittest
from unittest.mock import patch, MagicMock

from app27languages.app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch("psycopg2.connect")
    def test_get_languages(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "English", "2022-03-08 10:00:00")]

        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        response = self.app.get("/languages")
        data = json.loads(response.data)

        # mock_connect.assert_called_once()
        # mock_conn.cursor.assert_called_once()
        # mock_cursor.execute.assert_called_once_with("SELECT * FROM language")
        # mock_cursor.fetchall.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, [(1, "English", "2022-03-08T10:00:00")])


if __name__ == "__main__":
    unittest.main()
