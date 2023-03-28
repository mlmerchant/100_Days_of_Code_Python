import requests


def request_current_weather(lat, lng, api_key):
    # One Call API is no longer free. Using current weather instead.
    api_endpoint = "https://api.openweathermap.org/data/2.5/weather"
    payload = {
        'lat': str(lat),
        'lon': str(lng),
        'appid': api_key
    }

    response = requests.get(
        url=api_endpoint,
        params=payload)
    response.raise_for_status()
    data = response.json()
    return data
