import os
from twilio.rest import Client


def send_sms(to_number, from_number, msg):
    # TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN declared as environment variables.
    # Read more at http://twil.io/secure
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=msg,
        from_=from_number,
        to=to_number
    )
    print(message.status)
