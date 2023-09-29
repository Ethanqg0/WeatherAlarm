"""
Module: test_weather_api

This module contains unit tests for the functions in the 'src.weather_api' 
module. It utilizes the pytest framework to run a series of test cases to 
ensure the correctness of the weather and air quality data retrieval and 
grading functions.

Tested Functions:
- grade_aqi: Tests for grading Air Quality Index (AQI) values.
- get_clients: Tests for retrieving a list of clients.
- get_test_clients: Tests for retrieving a list of test clients.
- get_weather: Tests for retrieving weather data based on latitude 
and longitude.
- fetch_air_quality_data: Tests for fetching air quality data based on 
latitude and longitude.
- find_max_aqi: Tests for finding the maximum AQI value from provided data.

Each test case includes assertions to validate the expected behavior of the functions.
"""

import pytest
from src.weather_api import (
    grade_aqi,
    get_clients,
    get_test_clients,
    get_weather,
    fetch_air_quality_data,
    find_max_aqi,
)

@pytest.mark.parametrize("input_aqi, expected_grade", [
    (30, "- Great!"),
    (75, "- Moderate!"),
    (120, "- Unhealthy for Sensitive Groups!"),
    (180, "- Unhealthy!"),
    (250, "- Very Unhealthy!"),
    (350, "- Hazardous!"),
])
def test_grade_aqi(input_aqi, expected_grade):
    """
    Test the grade_aqi function.

    Args:
        input_aqi (int): The input Air Quality Index (AQI) value.
        expected_grade (str): The expected grade corresponding 
        to the input AQI.

    Returns:
        None
    """
    result = grade_aqi(input_aqi)
    assert result == expected_grade

def test_get_clients():
    """
    Test the get_clients function.

    Checks that the function returns a list of dictionaries, where 
    each dictionary represents a client.

    Returns:
        None
    """
    clients = get_clients()
    assert isinstance(clients, list)
    assert all(isinstance(client, dict) for client in clients)

def test_get_test_clients():
    """
    Test the get_test_clients function.

    Checks that the function returns a list of dictionaries, where 
    each dictionary represents a test client.

    Returns:
        None
    """
    test_clients = get_test_clients()
    assert isinstance(test_clients, list)
    assert all(isinstance(client, dict) for client in test_clients)

def test_get_weather():
    """
    Test the get_weather function.

    Checks that the function returns weather data in the form of a 
    dictionary when provided with valid latitude and longitude.

    Returns:
        None
    """
    latitude = 37.7749  # test latitude
    longitude = -122.4194  # test longitude
    weather_data = get_weather(latitude, longitude)
    assert isinstance(weather_data, dict)

def test_fetch_air_quality_data():
    """
    Test the fetch_air_quality_data function.

    Checks that the function returns air quality data in the form 
    of a dictionary when provided with valid latitude and longitude.

    Returns:
        None
    """
    latitude = 37.7749  # test value
    longitude = -122.4194  # test value
    air_quality_data = fetch_air_quality_data(latitude, longitude)
    assert isinstance(air_quality_data, dict)

def test_find_max_aqi():
    """
    Test the find_max_aqi function.

    Checks that the function correctly finds the maximum AQI 
    value from a given data dictionary.

    Returns:
        None
    """
    data = {"hourly": {"us_aqi": [10, 20, 5, 30, 15]}}
    max_aqi = find_max_aqi(data)
    assert max_aqi == 30
