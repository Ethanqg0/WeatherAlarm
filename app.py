from src.weatherAPI import *
import schedule
import time

# Production
def main():
    schedule.every().day.at("08:00").do(send_weather_update, get_clients())
    while True:
        schedule.run_pending()
        time.sleep(1)

#Instant testing
send_weather_update(get_test_clients())

if __name__ == "__main__":
    main()