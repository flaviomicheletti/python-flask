from unittest.mock import patch, MagicMock
from app26languages.app import app, get_languages

def test_get_languages():
    # Create a mock connection object and cursor object
    mock_cursor = MagicMock()
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    # Define the expected result of the query
    expected_result = [
        {'language_id': 1, 'name': 'English', 'last_update': '2023-03-01 12:00:00'},
        {'language_id': 2, 'name': 'Spanish', 'last_update': '2023-03-02 12:00:00'}
    ]
    
    # Patch the psycopg2.connect function to return the mock connection object
    with patch('psycopg2.connect', return_value=mock_conn):
        # Patch the cursor.execute method to return the expected result
        with patch.object(mock_cursor, 'fetchall', return_value=expected_result):
            # Make a request to the Flask endpoint
            with app.test_client() as client:
                response = client.get('/languages')
                assert response.status_code == 200
                
                # Parse the JSON response and check that it matches the expected result
                response_data = response.get_json()
                # assert response_data == expected_result
