from src.weatherAPI import grade_aqi
from config.supabase_config import *
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://wonclqrwdjpiodpgwbgs.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndvbmNscXJ3ZGpwaW9kcGd3YmdzIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ1NzI0OTAsImV4cCI6MjAxMDE0ODQ5MH0.fMJHVn5ECaWJA7pn18oPreKTCwtBS7g32N_M4NH55A8"
supabase = create_client(url, key)



def test_grade_aqi_good():
    result = grade_aqi(30)
    assert result == "- Great!"

def test_grade_aqi_moderate():
    result = grade_aqi(75)
    assert result == "- Moderate!"

def test_grade_aqi_unhealthy_sensitive_groups():
    result = grade_aqi(120)
    assert result == "- Unhealthy for Sensitive Groups!"

def test_grade_aqi_unhealthy():
    result = grade_aqi(180)
    assert result == "- Unhealthy!"

def test_grade_aqi_very_unhealthy():
    result = grade_aqi(250)
    assert result == "- Very Unhealthy!"

def test_grade_aqi_hazardous():
    result = grade_aqi(350)
    assert result == "- Hazardous!"
