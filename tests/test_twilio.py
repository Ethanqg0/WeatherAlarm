"""
Twilio Module

This module provides functionality to send text messages using the Twilio API.
It includes a function `send_text_message(body, to_phone)` that sends a text message
with the specified message body to the given phone number.
"""

from unittest.mock import Mock, patch
from src.twilio import send_text_message

def test_send_text_message():
    """
    Test function for the `send_text_message` function.

    This function mocks the TwilioClient and its methods to control the behavior and
    tests the `send_text_message` function's behavior. It checks whether the function correctly
    creates a message with the provided body and recipient phone number.
    """
    # Mock TwilioClient and its methods
    mock_twilio_client = Mock()
    mock_twilio_client.messages.create.return_value = Mock()

    with patch('src.twilio.TwilioClient', return_value=mock_twilio_client):
        # Define test input
        test_body = "This is a test message."
        test_phone = "+1234567890"

        # Call the function under test
        send_text_message(test_body, test_phone)

        # Assertions
        mock_twilio_client.messages.create.assert_called_with(
            body=test_body,
            from_="+0123456789", # hidden for security purposes
            to=test_phone
        )
