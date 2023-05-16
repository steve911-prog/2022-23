import requests

CITY = "kharkiv"
API = "49c620ef69a3645ac3037ba4962a366e"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API}&units=metric")

print(response.text)