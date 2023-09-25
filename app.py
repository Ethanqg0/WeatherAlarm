from src.weatherAPI import *
import schedule
import time

def main():
    schedule.every().day.at("06:00").do(send_weather_update, get_clients())
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()