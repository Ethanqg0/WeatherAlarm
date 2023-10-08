"""
Quotes Module

This module provides functions for retrieving random quotes from the Quotable API.
"""

import os
import requests

def get_quote(category, timeout=10) -> str:
    """
    Retrieves a random quote from the Quotable API.

    Args:
        category (str): The category of the quote.
        timeout (int, optional): The timeout for the HTTP request in seconds. Default is 10 seconds.

    Returns:
        str: A string containing the quote and author.
    """
    api_url = (
    f'https://api.api-ninjas.com/v1/quotes?'
    f'category={category}'
    )


    try:
        response = requests.get(
            api_url,
            headers={'X-Api-Key': "5iCq5Q3SIOSGkgRKo4j/LQ==HHD4GpRJPAgHUq62"},
            timeout=timeout
        )
        response.raise_for_status()
        data = response.json()
        print(data)
        quote = f"{data[0]['quote']} - {data[0]['author']}"
        return quote
    except requests.exceptions.RequestException as exception:
        print(f"HTTP request failed: {exception}")
        return "Failed to retrieve a quote"
