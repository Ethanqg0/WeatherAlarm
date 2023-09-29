import os
import dotenv
from twilio.rest import Client as TwilioClient

dotenv.load_dotenv()

def send_text_message(body: str, phone: str) -> None:
    """
    Sends a text message using Twilio's API.

    Args:
        body (str): The body of the text message.
        phone (str): The phone number to send the text message to.

    Returns:
        None
    """
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_phone_number = "+18333061864"
    to_phone_number = phone

    twilio_client = TwilioClient(account_sid, auth_token)

    message = twilio_client.messages.create(
        body=body,
        from_=from_phone_number,
        to=to_phone_number
    )
    print("Text message sent! :)")