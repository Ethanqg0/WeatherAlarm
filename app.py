import schedule
import time
import requests 
import re
from datetime import datetime
from twilio.rest import Client

def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&daily=sunrise,sunset&timezone=America%2FLos_Angeles"
    response = requests.get(base_url)
    data = response.json()
    return data

client_numbers = ["7089667431", "9254512502", "4159374283", "6307886898"]

def send_text_message(body):
    account_sid = "ACdfe74ca16e90ea5ecd2da2e5d9dd7321"
    auth_token = "9e43cec869d648e2a59811ced3172f67"
    from_phone_number = "+18333061864"
    to_phone_number = "7089667431"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_=from_phone_number,
        to=to_phone_number
    )
    print("Text message sent! :)")

def send_weather_update():
    latitude = 37.9891
    longitude = -122.0436

    weather_data = get_weather(latitude, longitude)

    temperature_celsius = weather_data["hourly"]["temperature_2m"][8]
    temperature_fahrenheit = round((temperature_celsius * 9/5) + 32)

    sunrise = weather_data["daily"]["sunrise"][0].split('T')[1]
    sunset = weather_data["daily"]["sunset"][0].split('T')[1]

    weather_info = {
        f"Good morning from Firewave! :)\n"
        f"Current Weather in Concord, CA:\n"
        f"Temperature: {temperature_fahrenheit}°F\n"
        f"Sunrise: {sunrise}\n"
        f"Sunset: {sunset}\n"
        f"Have a great day!\n\n\n"
    }

    send_text_message(weather_info)

send_weather_update()

"""
def main():
    schedule.every().day.at("08:00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
"""