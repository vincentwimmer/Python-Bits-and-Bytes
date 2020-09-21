import requests

weather = requests.get("https://wttr.in")

print(weather.text)
