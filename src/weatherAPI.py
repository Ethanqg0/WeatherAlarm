from config.supabase_config import *
from src.twilio import *
from src.quotes import *
import requests 
import dotenv

dotenv.load_dotenv()

def isGeneral(user_quote):
    if user_quote["isGeneral"] == "TRUE":
        return True
    else:
        return False

def get_clients():
    clients = Client.table("clients").select("*").execute().data
    return clients

def get_quotes():
    quotes = Client.table("quotes").select("*").execute().data
    return quotes

def match_quote(id):
    quotes = get_quotes()
    for quote in quotes:
        if quote['client'] == id:
            return quote["Text"]

def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&daily=sunrise,sunset&timezone=America%2FLos_Angeles"
    response = requests.get(base_url)
    data = response.json()
    return data

def fetch_air_quality_data(latitude, longitude):
    base_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={latitude}&longitude={longitude}&hourly=us_aqi&timezone=America%2FLos_Angeles"
    response = requests.get(base_url)
    data = response.json()
    return data

def find_max_aqi(data):
    us_aqi = data["hourly"]["us_aqi"]
    max_aqi = us_aqi[0]
    for aqi in us_aqi: 
        if aqi > max_aqi:
            max_aqi = aqi
    aqi = max_aqi
    return aqi

def grade_aqi(aqi):
    if aqi <= 50:
        return "- Great!"
    elif aqi <= 100:
        return "- Moderate!"
    elif aqi <= 150:
        return "- Unhealthy for Sensitive Groups!"
    elif aqi <= 200:
        return "- Unhealthy!"
    elif aqi <= 300:
        return "- Very Unhealthy!"
    else:
        return "- Hazardous!"
    

def send_weather_update(clients):
    for client in clients:
        if client['name'] == "Dylan":
            weather_data = get_weather(client['latitude'], client['longitude'])

            temperature_celsius = weather_data["hourly"]["temperature_2m"][6]
            temperature_fahrenheit = round((temperature_celsius * 9/5) + 32)

            peak_temperature = weather_data["hourly"]["temperature_2m"][14]
            peak_temperature_fahrenheit = round((peak_temperature * 9/5) + 32)

            sunrise = weather_data["daily"]["sunrise"][0].split('T')[1]
            sunset = weather_data["daily"]["sunset"][0].split('T')[1]

            aqi = fetch_air_quality_data(client['latitude'], client['longitude'])
            aqi = find_max_aqi(aqi)
            aqi = str(aqi) + grade_aqi(aqi)

            quote = match_quote(client['id'])

            """
            if quote['isGeneral'] == False:
                # if its specific, we need to append it to the ClientQuotes table
                Client.table("client_quotes").insert({"clientID": client['id'], "quoteID": quote["QuoteID"]}).execute()
            """
                
            weather_info = {
                f"Good morning! :)\n\n"
                f"Today's Weather in {client['city']}:\n"
                f"Current Temperature: {temperature_fahrenheit}°F\n"
                f"Peak Temperature: {peak_temperature_fahrenheit}°F\n"
                f"Sunrise: {sunrise}\n"
                f"Sunset: {sunset}\n"
                f"Air Quality: {aqi}\n\n"
                f"{quote}\n\n"
                f"Today is going to be a fantastic day. Make the best of it, {client['name']}!\n"
                f"From, Ethan\n\n\n"
            }
            send_text_message(weather_info, client['number'])
