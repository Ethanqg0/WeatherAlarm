from src.weatherAPI import grade_aqi, get_clients, get_test_clients, get_weather, fetch_air_quality_data, find_max_aqi
from config.supabase_config import *
from dotenv import load_dotenv
import pytest

# Load environmental variables from .env
load_dotenv()

url = "https://wonclqrwdjpiodpgwbgs.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndvbmNscXJ3ZGpwaW9kcGd3YmdzIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ1NzI0OTAsImV4cCI6MjAxMDE0ODQ5MH0.fMJHVn5ECaWJA7pn18oPreKTCwtBS7g32N_M4NH55A8"
supabase = create_client(url, key)

@pytest.mark.parametrize("input_aqi, expected_grade", [
    (30, "- Great!"),
    (75, "- Moderate!"),
    (120, "- Unhealthy for Sensitive Groups!"),
    (180, "- Unhealthy!"),
    (250, "- Very Unhealthy!"),
    (350, "- Hazardous!"),
])
def test_grade_aqi(input_aqi, expected_grade):
    result = grade_aqi(input_aqi)
    assert result == expected_grade

def test_get_clients():
    # Write test cases for get_clients function here
    # Use assert statements to check the expected results
    clients = get_clients()
    assert isinstance(clients, list)
    assert all(isinstance(client, dict) for client in clients)

def test_get_test_clients():
    # Write test cases for get_test_clients function here
    # Use assert statements to check the expected results
    test_clients = get_test_clients()
    assert isinstance(test_clients, list)
    assert all(isinstance(client, dict) for client in test_clients)

def test_get_weather():
    # Write test cases for get_weather function here
    # Use assert statements to check the expected results
    latitude = 37.7749  # Replace with a valid latitude
    longitude = -122.4194  # Replace with a valid longitude
    weather_data = get_weather(latitude, longitude)
    assert isinstance(weather_data, dict)
    # Add more assertions as needed

def test_fetch_air_quality_data():
    # Write test cases for fetch_air_quality_data function here
    # Use assert statements to check the expected results
    latitude = 37.7749  # Replace with a valid latitude
    longitude = -122.4194  # Replace with a valid longitude
    air_quality_data = fetch_air_quality_data(latitude, longitude)
    assert isinstance(air_quality_data, dict)
    # Add more assertions as needed

def test_find_max_aqi():
    # Write test cases for find_max_aqi function here
    # Use assert statements to check the expected results
    data = {"hourly": {"us_aqi": [10, 20, 5, 30, 15]}}
    max_aqi = find_max_aqi(data)
    assert max_aqi == 30  # The expected maximum AQI value