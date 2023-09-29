from src.weatherAPI import grade_aqi
from dotenv import load_dotenv
import pytest
import os

# Load environmental variables from .env file
load_dotenv('.env')

@pytest.fixture(autouse=True)
def load_environmental_variables(monkeypatch):
    # Set the environment variables for the tests
    monkeypatch.setenv('SUPABASE_URL', os.getenv('SUPABASE_URL'))
    monkeypatch.setenv('SUPABASE_KEY', os.getenv('SUPABASE_KEY'))

def test_grade_aqi_good():
    result = grade_aqi(30)
    assert result == "Good - Great!"

def test_grade_aqi_moderate():
    result = grade_aqi(75)
    assert result == "Moderate!"

def test_grade_aqi_unhealthy_sensitive_groups():
    result = grade_aqi(120)
    assert result == "Unhealthy for Sensitive Groups!"

def test_grade_aqi_unhealthy():
    result = grade_aqi(180)
    assert result == "Unhealthy!"

def test_grade_aqi_very_unhealthy():
    result = grade_aqi(250)
    assert result == "Very Unhealthy!"

def test_grade_aqi_hazardous():
    result = grade_aqi(350)
    assert result == "Hazardous!"
