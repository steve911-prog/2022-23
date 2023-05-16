import requests
import json

CITY = "kharkiv"
API = "2e500d85593210eabe2dd574e53fc677"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API}&units=metric")
data = json.loads(response.text)

print(data)