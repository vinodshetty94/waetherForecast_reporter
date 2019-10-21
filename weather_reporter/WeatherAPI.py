import requests
import json
from weather_reporter.APIEndPoints import APIEndPoints


class WeatherAPI:

    def __init__(self, name_of_place):
        result = requests.get(APIEndPoints.geolocation_api(name_of_place))
        latitude, longitude = APIEndPoints.get_lat_long(result.json())
        result = requests.get(APIEndPoints.weather_api(latitude, longitude))
        self.__weather_data = result.json()

    def __day_and_night_weather(self):
        return self.__weather_data['vt1dailyForecast']['day'], self.__weather_data['vt1dailyForecast']['night']

    def daily(self):
        day, night = self.__day_and_night_weather()

        data = dict()
        data['day'] = {key: day[key][0] for key in day.keys()}
        data['night'] = {key: night[key][0] for key in night.keys()}

        return data

    def week(self):
        day, night = self.__day_and_night_weather()

        data = dict()
        data['day'] = {key: day[key][:7] for key in day.keys()}
        data['night'] = {key: night[key][:7] for key in night.keys()}

        return data
        

    def five_days(self):
        day, night = self.__day_and_night_weather()

        data = dict()
        data['day'] = {key: day[key][:5] for key in day.keys()}
        data['night'] = {key: night[key][:5] for key in night.keys()}

        return data
        

    def month(self):
        day, night = self.__day_and_night_weather()

        data = dict()
        data['day'] = day
        data['night'] = night

        return data

    def json_dump(self, filename):
        with open(filename, 'w') as fh:
            json.dump(self.__weather_data, fh)

    def __str__(self):
        return str(self.__weather_data)
