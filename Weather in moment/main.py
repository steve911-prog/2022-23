import requests  #API
import json

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import sys


CITY = "kharkiv"
API = "2e500d85593210eabe2dd574e53fc677"

#get request to openweather
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API}&units=metric")


data = json.loads(response.text)

# print(data)

temp= data["main"]["temp"]
feels_like= data["main"]["feels_like"]
pressure= data["main"]["pressure"]
wind_speed= data["wind"]["speed"]
clouds= data["clouds"]
description = data["weather"][0]["description"]
icon= data["weather"][0]["icon"]

print(f"Temperature: {temp}\n{description}\nWind speed: {wind_speed}\nClouds: {clouds}")



class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("form.ui", self)
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec()