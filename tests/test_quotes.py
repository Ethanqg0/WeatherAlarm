"""
Quotes Module

This module provides functionality to fetch and process quotes from an external API.
It includes a function `get_quote(category)` that retrieves a quote from the API
based on the specified category.
"""

from unittest.mock import Mock, patch
from src.quotes import get_quote
from config.supabase_config import create_supabase_client

def test_get_quote():
    """
    Test function for the `get_quote` function.

    This function mocks the requests.get method to control the API response 
    and tests the behavior of the `get_quote` function. It checks whether 
    the function correctly processes the API response and returns the 
    expected result.

    Mocked behavior:
        - The 'requests.get' method is replaced with a Mock object to 
        simulate an API response.
        - The 'os.environ' dictionary is patched to set the 
        'QUOTES_API_KEY' environment variable.

    Test steps:
        1. Mock the 'requests.get' method to simulate the API response.
        2. Set the 'QUOTES_API_KEY' environment variable.
        3. Call the 'get_quote' function with a specified category.
        4. Compare the result with the expected quote string.

    Assertions:
        - Assert that the result matches the expected quote.

    Example Usage:
        To run this test, use a testing framework such as pytest:
        >>> pytest -v test_quotes_module.py

    """

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
