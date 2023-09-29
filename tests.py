from src.weatherAPI import grade_aqi
from config.supabase_config import *
import os

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(autouse=True)
def test_client_db():
    print(f"SUPABASE_URL"
          f"={os.environ.get('SUPABASE_URL')}")
    print(f"SUPAKEY={os.environ.get('SUPABASE_KEY')}")


def test():
    pass

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
