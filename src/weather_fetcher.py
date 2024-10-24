import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data():
    weather_data = {}
    for city in CITIES:
        params = {
            'q': f'{city},IN',
            'appid': API_KEY,
            'units': 'metric'  # This will return temperature in Celsius
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            weather_data[city] = response.json()
    return weather_data
