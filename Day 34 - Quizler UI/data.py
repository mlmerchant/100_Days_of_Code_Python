import requests

QUIZ_API = "https://opentdb.com/api.php"
PAYLOAD = {
    'amount': '10',
    'type': 'boolean'
}

response = requests.get(
    url=QUIZ_API,
    params=PAYLOAD)
response.raise_for_status()
data = response.json()
question_data = data['results']