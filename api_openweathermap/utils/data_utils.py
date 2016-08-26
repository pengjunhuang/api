from datetime_utils import time_converter
import pandas as pd


def data_organizer(api_data, type='dict', **kwargs):

    """
    :param api_data: dict-like ojbect obtained from api
    :param type str, choices from 'dict' and 'pd' or 'pandas'. Default 'dict'
    :return: output useful information from api json.
    """

    main = api_data.get('main')
    sys = api_data.get('sys')
    weather = api_data.get('weather')
    wind = api_data.get('wind')
    cloudiness = api_data.get('clouds')

    output_dict = dict(
        # city info
        city = api_data.get('name'),
        country = sys.get('country'),

        # Timestamp
        dt = time_converter(api_data.get('dt'), **kwargs),

        # temperature
        temp = main.get('temp'),
        temp_max = main.get('temp_max'),
        temp_min = main.get('temp_min'),

        # wind
        wind_speed = wind.get('speed'),
        wind_degree = wind.get('deg'),

        # weather condition
        humidity = main.get('humidity'),
        pressure = main.get('pressure'),
        sky = weather[0]['main'],

        # cloudiness
        cloudiness = cloudiness.get('all'),

        # sunrise and sunset
        sunrise = time_converter(sys.get('sunrise'), **kwargs),
        sunset = time_converter(sys.get('sunset'), **kwargs),
    )

    if type == 'pd' or type == 'pandas':
        return pd.DataFrame(output_dict, index=[0])
    else:
        return output_dict


def weather_reporter(data, unit):

    data['temp_symbol'] = u'\xb0'.encode('utf8') + map_unit(unit).get('temp')
    data['speed_symbol'] = map_unit(unit).get('speed')

    p = '''
        ---------------------------------------
        Current weather in: {city}, {country}:
        {temp}{temp_symbol}  {sky}
        Min: {temp_min}{temp_symbol}, Max: {temp_max}{temp_symbol}

        Wind Speed: {wind_speed} {speed_symbol}, Degree: {wind_degree}
        Humidity: {humidity}
        Cloudiness: {cloudiness}%
        Pressure: {pressure} hPa
        Sunrise at: {sunrise}
        Sunset at: {sunset}

        Last update from the server: {dt}
        ---------------------------------------'''
    return p.format(**data)


def map_unit(unit):

    mapping = {
        'imperial': {'temp': 'F', 'speed': 'mph'},
        'metric': {'temp': 'C', 'speed': 'm/s'},
    }

    return mapping.get(unit, {'temp': 'K', 'speed': 'm/s'})
