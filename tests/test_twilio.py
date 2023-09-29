import pytest
from unittest.mock import Mock, patch
from ..src.twilio import send_text_message

# Replace 'your_module' with the actual module or file where your function is defined.
#test

def test_send_text_message():
    # Mock TwilioClient and its methods
    mock_twilio_client = Mock()
    mock_twilio_client.messages.create.return_value = Mock()

    # Patch the TwilioClient constructor to return the mock TwilioClient
    with patch('src.twilio.TwilioClient', return_value=mock_twilio_client):
        # Define test input
        test_body = "This is a test message."
        test_phone = "+1234567890"

        # Call the function under test
        send_text_message(test_body, test_phone)

        # Assertions
        mock_twilio_client.messages.create.assert_called_with(
            body=test_body,
            from_="+18333061864",
            to=test_phone
        )
