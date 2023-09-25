from config.supabase_config import *
from src.twilio import *
import requests 

def get_clients():
    clients = Client.table("clients").select("*").execute().data
    return clients

def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&daily=sunrise,sunset&timezone=America%2FLos_Angeles"
    response = requests.get(base_url)
    data = response.json()
    return data

def send_weather_update(clients):
    for client in clients:
        weather_data = get_weather(client['latitude'], client['longitude'])

        temperature_celsius = weather_data["hourly"]["temperature_2m"][6]
        temperature_fahrenheit = round((temperature_celsius * 9/5) + 32)

        peak_temperature = weather_data["hourly"]["temperature_2m"][14]
        peak_temperature_fahrenheit = round((peak_temperature * 9/5) + 32)

        sunrise = weather_data["daily"]["sunrise"][0].split('T')[1]
        sunset = weather_data["daily"]["sunset"][0].split('T')[1]

        weather_info = {
            f"Good morning! :)\n"
            f"Today's Weather in {client['city']}:\n"
            f"Current Temperature: {temperature_fahrenheit}°F\n"
            f"Peak Temperature: {peak_temperature_fahrenheit}°F\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}\n"
            f"Today is going to be a fantastic day. Make the best of it, {client['name']}!\n"
            f"From, Ethan\n\n\n"
        }
        send_text_message(weather_info, client['number'])
