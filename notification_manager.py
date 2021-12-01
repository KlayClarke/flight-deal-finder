import os
import smtplib
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
PERSONAL_PHONE_NUMBER = os.environ.get('PERSONAL_PHONE_NUMBER')

MY_EMAIL = os.environ.get('MY_EMAIL')
MY_SECOND_EMAIL = os.environ.get('MY_SECOND_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')


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

    def send_email(self, email_text):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_SECOND_EMAIL, msg=email_text)


