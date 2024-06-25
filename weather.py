import requests


def get_weather(location, units='metric'):
    api_key = 'OPENWEATHER_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&units={units}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data
