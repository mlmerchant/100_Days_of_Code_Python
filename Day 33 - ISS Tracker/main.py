import os
from time import sleep

SUNRISE_API_ENDPOINT = "https://api.sunrise-sunset.org/json"
ISS_API_ENDPOINT = "http://api.open-notify.org/iss-now.json"
LATITUDE: float = 30.497002
LONGITUDE: float = -86.13391

# Never Hard Code Credentials!
# password is app password - follow URL returned in the error message.
my_email = os.environ.get('MY_EMAIL')
password = os.environ.get('PASSWORD')
to_email = os.environ.get('TO_EMAIL')


def send_mail(from_address, email_provider, to_address, subject, text):
    """Send email from Google, Hotmail, or Yahoo using SMTP."""
    import smtplib
    message = "Subject:" + subject + "\n\n" + text
    if email_provider == "Google":
        smtp_server = "smtp.gmail.com"
    elif email_provider == "Hotmail":
        smtp_server = "smtp.live.com"
    elif email_provider == "Yahoo":
        smtp_server = "smtp.mail.yahoo.com"
    with smtplib.SMTP(smtp_server) as connection:
        connection.starttls()
        connection.login(user=from_address, password=password)
        connection.sendmail(
            from_addr=from_address,
            to_addrs=to_address,
            msg=message
        )


def get_sunrise_and_sunset(lat, long):
    import requests
    """Return a tuple containing the sunrise and sunset times for the given lat/long."""
    payload = {
        'lat': lat,
        'lng': long,
        'formatted': 0
    }
    response = requests.get(
        url=SUNRISE_API_ENDPOINT,
        params=payload)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    return sunrise, sunset


def get_iss_location():
    import requests
    """Returns a tuple with the current lat/long of the international space station as a float."""
    response = requests.get(url=ISS_API_ENDPOINT)
    response.raise_for_status()
    data = response.json()
    lat = float(data["iss_position"]["latitude"])
    long = float(data["iss_position"]["longitude"])
    return long, lat


def is_night(lat, long, offset):
    """Return True if it is currently night for the given lat/long."""
    import datetime
    now = datetime.datetime.now()
    sunrise_and_sunset = get_sunrise_and_sunset(lat=LATITUDE, long=LONGITUDE)
    sunrise_hour = int(sunrise_and_sunset[0].split("T")[1].split(":")[0]) + offset
    sunset_hour = int(sunrise_and_sunset[1].split("T")[1].split(":")[0]) + offset
    sunrise_minute = int(sunrise_and_sunset[0].split("T")[1].split(":")[1])
    sunset_minute = int(sunrise_and_sunset[1].split("T")[1].split(":")[1])

    if sunrise_hour < 0:
        sunrise_hour += 24
    if sunset_hour < 0:
        sunset_hour += 24

    if now.hour < sunrise_hour:
        return True
    if now.hour > sunset_hour:
        return True
    if now.hour == sunset_hour:
        if now.minute >= sunset_minute:
            return True
        else:
            return False
    if now.hour == sunrise_hour:
        if now.minute < sunrise_minute:
            return True
        else:
            return False
    else:
        return False


def is_close_enough(lat_long1, lat_long2, distance=5):
    lat1 = lat_long1[0]
    lng1 = lat_long1[1]
    lat2 = lat_long2[0]
    lng2 = lat_long2[1]

    lat_distance = abs(lat1 - lat2)
    long_distance = abs(lng1 - lng2)

    print("Latitude distance is: ", lat_distance)
    print("Longitude distance is: ", long_distance)

    if lat_distance <= distance and long_distance <= distance:
        return True
    else:
        return False


def send_email_if_iss_overhead():
    current_location = (LATITUDE, LONGITUDE)
    if is_close_enough(lat_long1=current_location, lat_long2=get_iss_location()):
        if is_night(lat=LATITUDE, long=LONGITUDE, offset=-5):
            print("Look up! The ISS is overhead!")
            send_mail(
                from_address=my_email,
                email_provider="Google",
                to_address=my_email,
                subject="Look up! ISS is overhead!",
                text="Look up! The ISS is passing by in the night sky!"
            )
            return True
        else:
            print("The ISS is overhead, but it isn't night.")
            return False
    else:
        print("The ISS is too far away!")
        return False


while True:
    send_email_if_iss_overhead()
    sleep(60)




