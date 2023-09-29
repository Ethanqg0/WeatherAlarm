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
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'  
    
    try:
        response = requests.get(api_url, headers={'X-Api-Key': os.getenv('QUOTES_API_KEY') }, timeout=timeout)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        print(data)
        quote = f"{data[0]['quote']} - {data[0]['author']}"  # Use an f-string here
        return quote
    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
        return "Failed to retrieve a quote"