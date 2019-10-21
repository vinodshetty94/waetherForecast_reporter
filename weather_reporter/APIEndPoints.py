class APIEndPoints:
    
    __GET_GEOLOCATION_API = 'https://api.weather.com/v3/location/search?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&language=en-IN&locationType=locale&query={name_of_place}'

    __GET_WEATHER_DATA = 'https://api.weather.com/v2/turbo/vt1dailyForecast?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&geocode={geo_location}&language=en-IN&units=m'

    @classmethod
    def geolocation_api(cls, name_of_place) -> str:
        name_of_place = str(name_of_place).replace(' ', '%20')
        return cls.__GET_GEOLOCATION_API.format(name_of_place=name_of_place)

    @classmethod
    def weather_api(cls, latitude, longitude) -> str:
        geo_location = f'{latitude}%2C{longitude}'
        return cls.__GET_WEATHER_DATA.format(geo_location=geo_location)

    @staticmethod
    def get_lat_long(json_data):
        return json_data['location']['latitude'][0], json_data['location']['longitude'][0]
