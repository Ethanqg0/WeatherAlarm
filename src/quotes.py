import requests

def get_quote() -> str:
    """
    Retrieves a random quote from the Quotable API.

    Returns:
        str: A string containing the quote and author.
    """
    api_url = "https://api.quotable.io/quotes/random"
    response = requests.get(api_url)
    data = response.json()
    quote = data[0]["content"] + " - " + data[0]["author"]
    return quote