from unittest.mock import MagicMock, patch
from app26languages.app import app

def test_get_languages(client):
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        (1, 'English', '2022-01-01 00:00:00'),
        (2, 'Spanish', '2022-01-01 00:00:00'),
        (3, 'French', '2022-01-01 00:00:00'),
    ]
    with patch('psycopg2.connect') as mock_connect:
        mock_connect.return_value.cursor.return_value = mock_cursor
        response = client.get('/languages')
    assert response.status_code == 200
    assert response.json == [
        {'language_id': 1, 'name': 'English', 'last_update': '2022-01-01 00:00:00'},
        {'language_id': 2, 'name': 'Spanish', 'last_update': '2022-01-01 00:00:00'},
        {'language_id': 3, 'name': 'French', 'last_update': '2022-01-01 00:00:00'},
    ]
