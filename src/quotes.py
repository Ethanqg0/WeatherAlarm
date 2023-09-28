import requests

def get_quote():
    api_url = "https://api.quotable.io/quotes/random"
    response = requests.get(api_url)
    data = response.json()
    quote = data[0]["content"] + " - " + data[0]["author"]
    return quote