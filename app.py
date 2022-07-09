import requests
import configparser
from flask import Flask, render_template


app = Flask(__name__)

config = configparser.ConfigParser()
config.read('settings.ini')

API_KEY = config.get('OPEN_WEATHER', 'API_KEY')


@app.route('/')
def index():
    geo_url = 'https://get.geojs.io/v1/ip/geo.json'

    response = requests.get(geo_url)

    geo_data = response.json()

    lat = geo_data['latitude']
    lon = geo_data['longitude']

    weather_url = (
        f'http://api.openweathermap.org/data/2.5/weather?'
        f'lat={lat}&lon={lon}&appid={API_KEY}')

    response = requests.get(weather_url)

    weather_data = response.json()

    country = weather_data['sys']['country']
    city = weather_data['name']
    img = weather_data['weather'][0]['icon']
    weather = weather_data['weather'][0]['main']
    description = weather_data['weather'][0]['description']

    img_url = f'http://openweathermap.org/img/w/{img}.png'

    return render_template(
        'index.html', 
        country=country, 
        city=city, 
        img_url=img_url, 
        weather=weather, 
        description=description,
        data=weather_data)


if __name__ == '__main__':
    app.run()
