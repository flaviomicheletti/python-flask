import unittest
from unittest.mock import patch, MagicMock
from foo.main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('foo.db.connect', new_callable=MagicMock)
    def test_languages(self, mock_connect):
        # Mocking the cursor and execute method
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("English",), ("Spanish",)]
        mock_connect.return_value.cursor.return_value = mock_cursor

        response = self.app.get("/languages", content_type="application/json")
        self.assertEqual(response.status_code, 200)

        # Assert that the mocked functions were called as expected
        mock_connect.assert_called_once()
        mock_connect.return_value.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM languages")
        mock_cursor.fetchall.assert_called_once()


#
# 100% coverage
#