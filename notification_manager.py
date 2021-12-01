import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
PERSONAL_PHONE_NUMBER = os.environ.get('PERSONAL_PHONE_NUMBER')


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_sms(self, sms_text):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=sms_text,
            from_=TWILIO_PHONE_NUMBER,
            to=PERSONAL_PHONE_NUMBER)
        print(message)
