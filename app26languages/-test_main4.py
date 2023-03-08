import pytest
from flask import Flask
from unittest.mock import MagicMock
from app26languages.app import get_languages

@pytest.fixture
def app():
    app = Flask(__name__)
    return app

def test_get_languages(app, mock):
    # Set up mock database connection
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        (1, 'Python', '2022-01-01 00:00:00'),
        (2, 'Java', '2022-01-02 00:00:00'),
        (3, 'C++', '2022-01-03 00:00:00')
    ]
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock.patch('psycopg2.connect', return_value=mock_conn)

    # Call get_languages() function and check response
    response = get_languages()
    assert response.status_code == 200
    assert response.get_json() == [
        {'language_id': 1, 'name': 'Python', 'last_update': '2022-01-01 00:00:00'},
        {'language_id': 2, 'name': 'Java', 'last_update': '2022-01-02 00:00:00'},
        {'language_id': 3, 'name': 'C++', 'last_update': '2022-01-03 00:00:00'}
    ]
