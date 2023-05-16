import requests
import json

CITY = "kharkiv"
API = "2e500d85593210eabe2dd574e53fc677"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API}&units=metric")
data = json.loads(response.text)

print(data)

temp= data["main"]["temp"]
feels_like= data["main"]["feels_like"]
pressure= data["main"]["pressure"]
wind_speed= data["wind"]["speed"]
clouds= data["clouds"]
description = data["weather"][0]["description"]
icon= data["weather"][0]["icon"]
