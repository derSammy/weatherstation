import requests

API_KEY = ''

CITY = 'DRESDEN'

url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

res = requests.get(url)
data = res.json()

humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind = data['wind']['speed']
description = data['weather'][0]['description']
temp = data['main']['temp']

print('Temperature:',temp,'°C')
print('Wind:',wind)
print('Pressure: ',pressure)
print('Humidity: ',humidity)
print('Description:',description)
