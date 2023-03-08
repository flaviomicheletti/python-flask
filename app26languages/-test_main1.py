import json
from unittest.mock import patch, Mock
from app26languages.app import app

def test_get_languages():
    # Create a mock database connection object
    mock_conn = Mock()

    # Replace the psycopg2.connect() function with a function that returns the mock connection object
    with patch('psycopg2.connect', return_value=mock_conn):
        # Create a test client for the Flask application
        client = app.test_client()

        # Send a GET request to the /languages endpoint and retrieve the response
        response = client.get('/languages')

        # Convert the response data from JSON to a Python object
        data = json.loads(response.data)

        # Test the content of the response data
        assert response.status_code == 200
        assert len(data) == 0 # No data since mock connection
