# Import your grade_aqi function at the beginning of your test file

from src.weatherAPI import grade_aqi
from dotenv import load_dotenv
from config.supabase_config import *
import pytest
import os

load_dotenv()

@pytest.fixture(autouse=True) #autoamtically uses the fixture
def load_environmental_variables(monkeypatch):
    load_dotenv('.env.test')

    # Set the environment variables for the tests
    monkeypatch.setenv('SUPABASE_URL', os.getenv('SUPABASE_URL'))
    monkeypatch.setenv('OTHER_VARIABLE', os.getenv('OTHER_VARIABLE'))

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
