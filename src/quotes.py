import requests
import os

def get_quote(category) -> str:
    """
    Retrieves a random quote from the Quotable API.

    Returns:
        str: A string containing the quote and author.
    """
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': os.getenv('QUOTES_API_KEY') })
    data = response.json()
    print(data)
    quote = data[0]['quote'] + " - " + data[0]['author']
    return quote