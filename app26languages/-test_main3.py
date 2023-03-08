import pytest
from unittest.mock import patch, MagicMock
from app26languages.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        with patch('psycopg2.connect') as mock_connect:
            mock_cursor = MagicMock()
            mock_fetchall = MagicMock()
            mock_cursor.fetchall.return_value = mock_fetchall
            mock_connect.return_value.cursor.return_value = mock_cursor
            yield client

def test_get_languages(client):
    mock_fetchall = [('1', 'Python', '2022-03-01'), ('2', 'JavaScript', '2022-03-02')]
    client.get('/languages')
    assert client.status_code == 200
    assert client.json == [{'language_id': '1', 'name': 'Python', 'last_update': '2022-03-01'},
                           {'language_id': '2', 'name': 'JavaScript', 'last_update': '2022-03-02'}]
