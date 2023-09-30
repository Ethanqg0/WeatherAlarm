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
Follow these steps to set up and run WeatherAlarm:

1. **Clone the Repository:** Begin by cloning this repository to your local machine using your preferred Git client.

2. **Install Dependencies:** Navigate to the cloned repository and install the necessary dependencies.

3. **Configuration:** Set up configuration files to specify API keys and user preferences. Ensure Twilio API credentials are properly configured.

4. **Customization:** Customize the messages, weather preferences, and motivational quotes based on user preferences.

5. **Run the Application:** Execute the application to send morning messages to users at 8 AM.
  A. Create a virtual environment and run it
  Linux/macOS:
  ```
  python -m venv venv
  source venv/bin/activate
  ```
  Windows:
  ```
  python3 -m venv venv
  .\venv\Scripts\Activate.ps1 (powershell) or venv\Scripts\activate.ps1 (command prompt)
  ```

  B. Install dependencies
  ```
  pip install -r requirements.txt
  ```

  C. Run app
  ```
  python app.py
  ```

## Usage
WeatherAlarm is designed to be simple and user-friendly. Users will receive a personalized morning message at 8 AM containing weather information, air quality data, and a motivational quote. They can respond with specific preferences and receive tailored messages accordingly.

Contributing
We welcome contributions from the community! Whether you're a developer, designer, or have ideas to enhance the project, your insights are valuable. Join our vibrant community by submitting pull requests, sharing ideas, and participating in discussions.

## Contact Us
Have questions or need assistance? Reach out to our team at ethan@firewave.dev

Let's make mornings brighter with WeatherAlarm! Happy messaging!
