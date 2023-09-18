import schedule
import time
import requests 
import re
from datetime import datetime
from twilio.rest import Client as TwilioClient
from supabase import create_client, Client

url = "https://wonclqrwdjpiodpgwbgs.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndvbmNscXJ3ZGpwaW9kcGd3YmdzIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ1NzI0OTAsImV4cCI6MjAxMDE0ODQ5MH0.fMJHVn5ECaWJA7pn18oPreKTCwtBS7g32N_M4NH55A8"
Client = create_client(url, key)

def get_clients():
    clients = Client.table("clients").select("*").execute().data
    return clients

def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&daily=sunrise,sunset&timezone=America%2FLos_Angeles"
    response = requests.get(base_url)
    data = response.json()
    return data

def send_text_message(body, phone):
    account_sid = "ACdfe74ca16e90ea5ecd2da2e5d9dd7321"
    auth_token = "9e43cec869d648e2a59811ced3172f67"
    from_phone_number = "+18333061864"
    to_phone_number = phone

    twilio_client = TwilioClient(account_sid, auth_token)

    message = twilio_client.messages.create(
        body=body,
        from_=from_phone_number,
        to=to_phone_number
    )
    print("Text message sent! :)")


def send_weather_update(clients):
    for client in clients:
        weather_data = get_weather(client['latitude'], client['longitude'])

        temperature_celsius = weather_data["hourly"]["temperature_2m"][13]
        temperature_fahrenheit = round((temperature_celsius * 9/5) + 32)

        sunrise = weather_data["daily"]["sunrise"][0].split('T')[1]
        sunset = weather_data["daily"]["sunset"][0].split('T')[1]

        weather_info = {
            f"Good morning from Firewave! :)\n"
            f"Today's Weather in {client['city']}:\n"
            f"Current Temperature: {temperature_fahrenheit}°F\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}\n"
            f"Have a great day, {client['name']}!\n\n\n"
        }

        send_text_message(weather_info, client['number'])

send_weather_update(get_clients())