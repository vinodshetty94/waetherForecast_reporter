from weather_reporter.WeatherAPI import WeatherAPI


class WeatherApp:

    @staticmethod
    def get_weather_info(query, date=None, type='daily'):

        weather = WeatherAPI(query)

        if type == 'five_days':
            return weather.five_days()
        elif type == 'month':
            return weather.month()
        elif type == 'week':
            return weather.week()
        else:
            return weather.daily()
