import pytest
from unittest.mock import Mock, patch
from ..src.quotes import get_quote

def test_get_quote():
    # Mock the requests.get method to control the API response
    mock_response = Mock()
    mock_response.json.return_value = [
        {
            'quote': 'Test quote',
            'author': 'Test author'
        }
    ]

    with patch('src.quotes.requests.get', return_value=mock_response):
        # Set the environment variable for the API key
        with patch.dict('os.environ', {'QUOTES_API_KEY': 'your_api_key'}):
            # Call the function under test
            result = get_quote('category')

    # Assertions
    expected_quote = 'Test quote - Test author'
    assert result == expected_quote
