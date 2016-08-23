import argparse

from config import global_settings
from utils.api_utils import get_api_data
from utils.data_utils import data_organizer, weather_reporter

class CurrentWeather(object):
    user_api = global_settings.get('user_api')
    api_main = global_settings.get('api_main')

    def __init__(self, city_name, unit='imperial', output_type='dict'):
        self.city_name = city_name
        self.unit = unit
        self.output_type = output_type

    def get_api_url(self):
        city_name = self.city_name.replace(' ', '%20')
        mode = 'json'
        api_url = "{}q={}&units={}&mode={}&appid={}".format(self.api_main, city_name, self.unit, mode, self.user_api)
        return api_url

    def get_data(self):
        return get_api_data(self.get_api_url())

    def get_weather(self):
        return data_organizer(self.get_data(), self.output_type)

    def report_weather(self):
        weather_dict = data_organizer(self.get_data(), 'dict')
        return weather_reporter(weather_dict)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate weather report from Openweathermap API')
    parser.add_argument('city_name', nargs='?', type=str, default='san francisco')
    parser.add_argument('unit', nargs='?', type=str, default='imperial')
    parser.add_argument('output_type', nargs='?', type=str, default='dict')

    args = parser.parse_args()

    city_weather = CurrentWeather(args.city_name, args.unit, args.output_type)
    print city_weather.report_weather()
