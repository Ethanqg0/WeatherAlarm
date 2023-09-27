from src.weatherAPI import *
import schedule
import time
import dotenv

dotenv.load_dotenv()

def main():
    schedule.every().day.at("08:00").do(send_weather_update, get_clients())
    while True:
        schedule.run_pending()
        time.sleep(1)

send_weather_update(get_clients())