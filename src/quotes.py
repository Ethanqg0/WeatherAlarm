import requests

def get_quote(category):
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
    data = response.json()
    quote = data[0]['quote'] + " - " + data[0]['author']
    return quote
