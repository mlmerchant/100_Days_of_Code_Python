import os
from weather_data import request_current_weather
from twilio_sms import send_sms

LATITUDE: float = 40.57464
LONGITUDE: float = -122.38109

API_KEY = os.environ.get('API_KEY')
TO_PHONE_NUMBER = os.environ.get('TO_PHONE_NUMBER')
FROM_PHONE_NUMBER = os.environ.get('FROM_PHONE_NUMBER')

weather_data = request_current_weather(lat=LATITUDE, lng=LONGITUDE, api_key=API_KEY)

is_raining = False
# less than 700 means rain or snow.
for x in weather_data['weather']:
    if int((x['id'])) < 700:
        is_raining = True
        break

if is_raining:
    print("Bring an umbrella!")
    send_sms(
        to_number=TO_PHONE_NUMBER,
        from_number=FROM_PHONE_NUMBER,
        msg="Bring an umbrella! ☂️"
    )
else:
    print("No rain detected.")
