import requests

s_city = "Moscow,RU"
appid = '61b5e2c5a04b191361dacc1ac177ed5d'


res = requests.get("http://api.openweathermap.org/data/2.5/weather",params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
a = "Город:", s_city
b = "Температура:", data['main']['temp']
c = "Видимость",data["visibility"]
d = 'Влажность',data['main']['humidity']

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("Прогноз погоды на неделю:")
for i in data['list']:
    x = i['dt_txt']
    if x == '2022-11-17 09:00:00' or x ==  '2022-11-17 12:00:00' or x =='2022-11-17 18:00:00':
        print("Время <", x,"> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),
              "> \r\nВидимость <",i['visibility'], "> \r\nВлажность <",i['main']['humidity'],">")
        print("____________________________")