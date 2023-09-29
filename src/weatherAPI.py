"""
This module provides functions for retrieving weather and air quality data, grading AQI values,
and sending weather updates to clients.

Modules imported:
- `config.supabase_config`: Configuration for Supabase database.
- `src.twilio`: Functions for sending text messages via Twilio.
- `src.quotes`: Functions for retrieving inspirational quotes.
- `requests`: HTTP library for making API requests.
- `dotenv`: Loading environment variables from a .env file.

Functions provided:
- `get_clients() -> list`: Retrieves a list of clients from the Supabase database.

- `get_test_clients()`: Retrieves test clients' data from the Supabase database.

- `get_weather(latitude: float, longitude: float) -> dict`: Retrieves weather data
  from the Open Meteo API for a given latitude and longitude.

- `fetch_air_quality_data(latitude: float, longitude: float) -> dict`: Retrieves air quality data
  from the Open Meteo API for a given latitude and longitude.

- `find_max_aqi(data: dict) -> int`: Finds the maximum AQI value in the hourly US AQI data.

- `grade_aqi(aqi: int) -> str`: Assigns a grade to an AQI value.

- `send_weather_update(clients: list) -> None`: Sends a weather update to a list of clients.

For more information on each function, refer to their respective docstrings.
"""

from config.supabase_config import *
from src.twilio import *
from src.quotes import *
import requests
import dotenv

dotenv.load_dotenv()

def get_clients() -> list:
    """
    Retrieves a list of clients from the Supabase database.

    Returns:
        list: A list of dictionaries representing the clients.
    """
    return Client.table("clients").select("*").execute().data

def get_test_clients():
    return Client.table("test_clients").select("*").execute().data

def get_weather(latitude: float, longitude: float) -> dict:
    """
    Retrieves weather data from the Open Meteo API for a given latitude and longitude.

    Args:
        latitude (float): The latitude of the location to retrieve weather data for.
        longitude (float): The longitude of the location to retrieve weather data for.

    Returns:
        dict: A dictionary containing weather data for the specified location.
    """
    base_url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&hourly=temperature_2m&daily=sunrise,sunset"
    f"&timezone=America%2FLos_Angeles"
    )

    response = requests.get(base_url)
    data = response.json()
    return data

def fetch_air_quality_data(latitude: float, longitude: float) -> dict:
    """
    Retrieves air quality data from the Open Meteo API for a given latitude and longitude.

    Args:
        latitude (float): The latitude of the location to retrieve air quality data for.
        longitude (float): The longitude of the location to retrieve air quality data for.

    Returns:
        dict: A dictionary containing air quality data for the specified location.
    """
    base_url = (
    f"https://air-quality-api.open-meteo.com/v1/air-quality?"
    f"latitude={latitude}&longitude={longitude}"
    f"&hourly=us_aqi&timezone=America%2FLos_Angeles"
    )
    response = requests.get(base_url)
    data = response.json()
    return data

def find_max_aqi(data: dict) -> int:
    """
    Finds the maximum AQI value in the hourly US AQI data.

    Args:
        data (dict): A dictionary containing hourly US AQI data.

    Returns:
        int: The maximum AQI value.
    """
    us_aqi = data["hourly"]["us_aqi"]
    max_aqi = us_aqi[0]
    for aqi in us_aqi:
        if aqi is None:
            continue
        if aqi > max_aqi:
            max_aqi = aqi
    return max_aqi

def grade_aqi(aqi: int) -> str:
    """
    Assigns a grade to an AQI value.

    Args:
        aqi (int): The AQI value to grade.

    Returns:
        str: A string representing the grade of the AQI value.
    """
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

def send_weather_update(clients: list) -> None:
    """
    Sends a weather update to a list of clients.

    Args:
        clients (list): A list of dictionaries representing the clients.

    Returns:
        None
    """
    for client in clients:
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

        quote = get_quote(client['category'])

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
            f"From, WeatherAlarm\n\n\n"
        }
    send_text_message(weather_info, client['number'])
