"""
Weather Update Scheduler

This module schedules and sends daily weather updates to clients using a weather API.
It defines a main function for production use and a test call for instant testing.

Author:
    Ethan Gutierrez - Ethanqg0
"""

import time
import schedule
from src.weather_api import send_weather_update, get_clients, get_test_clients

# Production
def main():
    """
    Schedule and execute a daily weather update task.

    This function uses the `schedule` library to schedule a daily task that sends 
    a weather update to clients at 08:00 AM. The weather update is obtained by 
    calling the `send_weather_update` function with the list of
    clients obtained from the `get_clients` function.

    The function runs indefinitely, continuously checking for pending scheduled 
    tasks and sleeping for one second between checks.
    """
    schedule.every().day.at("08:00").do(send_weather_update, get_clients())
    while True:
        schedule.run_pending()
        time.sleep(1)

#Instant testing
send_weather_update(get_test_clients())
#test

if __name__ == "__main__":
    main()
