# Tutorial made by NeuralNine on YouTube
import os
import datetime
from http.client import responses

import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY_PATH = os.path.expanduser('~/Desktop/API/api_key_openweathermap')
API_KEY = open(API_KEY_PATH, 'r').read().strip()
CITY = input("Enter the city of your choice: ").capitalize()

def kelvin_to_celsius_farenheit(kelvin):
    celsius = kelvin - 237.15
    farenheit = celsius * (9/5) + 32
    return celsius, farenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_celsius, temp_farenheit = kelvin_to_celsius_farenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_farenheit = kelvin_to_celsius_farenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = datetime.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = datetime.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_farenheit:.2f}°F")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C or {feels_like_farenheit:.2f}°F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}km/h")
print(f"General Weather in {CITY}: {description}")
print(f"The sun rises in {CITY}: at {sunrise_time} local time.")
print(f"The sun sets in {CITY}: at {sunset_time} local time.")

