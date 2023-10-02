# WeatherAlarm
Welcome to the WeatherAlarm project! WeatherAlarm is a minimalistic and customizable weather notification system that sends users personalized morning messages at 8 AM. It provides weather information, air quality data for environmental awareness, and a motivational quote. WeatherAlarm fetches this information from external APIs and tailors it to each user's preferences.

<img src="./assets/ai.jpg" alt="Logo Image" width="300" height="250">

## Features
- **Personalized Messages:** WeatherAlarm addresses users by their name and delivers a customized morning message.

- **Weather Information:** Users receive up-to-date weather details for their location or a location of their choice.

- **Air Quality Data:** WeatherAlarm provides air quality information to promote environmental consciousness.

- **Motivational Quotes:** Users can choose between general or zen motivational quotes to kickstart their day.

- **Customization:** Users can specify their preferences for weather information and motivational quotes.

- **Twilio Integration:** WeatherAlarm utilizes the Twilio messaging service to send SMS messages to users.

## Getting Started

WeatherAlarm is open-source and highly encourages contributions! To pursue this, we containerized WeatherAlarm via Docker to ensure its portability and convenience! Here are the steps:

Prerequisite:
  Have Docker installed on your computer and running to activate its Daemon.

#1: Pull the Pre-Built Docker Image
To get started, you can pull the pre-built Docker image from the container registry (e.g., Docker Hub) using the following command:
```
docker push ethanqg/weatheralarm:v1.0
```

#2:Run the Docker Container
```
docker container run -d ethanqg/weatheralarm:v1.0
```

Access the Application
After running the container, you can access the application as needed.

## Usage
WeatherAlarm is designed to be simple and user-friendly. Users will receive a personalized morning message at 8 AM containing weather information, air quality data, and a motivational quote. They can respond with specific preferences and receive tailored messages accordingly.

## Contact Us
Have questions or need assistance? Reach out to our team at ethan@firewave.dev

Let's make mornings brighter with WeatherAlarm! Happy messaging!
