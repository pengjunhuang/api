import argparse

from config import global_settings
from utils.api_utils import get_api_data
from utils.data_utils import data_organizer, weather_reporter


class CurrentWeather(object):
    user_api = global_settings.get('user_api')
    api_main = global_settings.get('api_main')

    def __init__(self, city_name, unit='imperial', output_type='dict', timezone='America/Los_Angeles', offset=0):
        """

        :param city_name, e.g. sanfrancisco,us
        :param unit, imperial for Fahrenheit, metric for Celsius, default is Kelvin
        :param output_type, choices of dict and pd (or pandas)
        :param timezone, time zone default is America/Los_Angeles
        :param offset, optional, used when user does not know the timezone and need to adjust time manually
        """

        self.city_name = city_name
        self.unit = unit
        self.output_type = output_type
        self.timezone = timezone
        self.offset = offset

    def get_api_url(self):
        city_name = self.city_name.replace(' ', '%20')
        mode = 'json'
        api_url = "{}q={}&units={}&mode={}&appid={}".format(self.api_main, city_name, self.unit, mode, self.user_api)
        return api_url

    def get_data(self):
        return get_api_data(self.get_api_url())

    def get_weather(self):
        return data_organizer(self.get_data(), self.output_type, timezone=self.timezone, offset=self.offset)

    def report_weather(self):
        weather_dict = data_organizer(self.get_data(), 'dict', timezone=self.timezone, offset=self.offset)
        return weather_reporter(weather_dict, self.unit)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate current weather report from Openweathermap API')

    parser.add_argument('city_name', nargs='?', type=str, default='san francisco, us',
                        help='city name with the format like city,country')
    parser.add_argument('-c', dest='unit', nargs='?', const='metric', default='imperial',
                        help='unit of metrics, optional for Celsius and m/s. Default is Fahrenheit and mph')
    parser.add_argument('-o', dest='offset', nargs='?', type=int, const=0, default=0,
                        help='hour offset from the Pacific time')
    parser.add_argument('-tz', dest='timezone', nargs='?', type=str, const='America/Los_Angeles', default='America/Los_Angeles',
                        help='time zone in pytz module, default as Pacific Time')

    args = parser.parse_args()

    city_weather = CurrentWeather(city_name=args.city_name,
                                  unit=args.unit,
                                  timezone=args.timezone,
                                  offset=args.offset)

    print city_weather.report_weather()
