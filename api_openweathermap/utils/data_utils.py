from datetime_utils import time_converter
import pandas as pd


def data_organizer(api_data, type = 'dict'):
    '''

    :param api_data: dict-like ojbect obtained from api
    :param type: str, choices from 'dict' and 'pd' or 'pandas'. Default 'dict'
    :return: output useful information from api json.
    '''

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
        dt = time_converter(api_data.get('dt')),

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
        sunrise = time_converter(sys.get('sunrise'), format =  '%I:%M %p'),
        sunset = time_converter(sys.get('sunset'), format = '%I:%M %p'),
    )

    if type == 'pd' or type == 'pandas':
        return pd.DataFrame(output_dict, index=[0])
    else:
        return output_dict

def weather_reporter(data):
    # TODO:Hardcoded units

    data['m_symbol'] = u'\xb0'.encode('utf8') + 'F'
    s = '''
        ---------------------------------------
        Current weather in: {city}, {country}:
        {temp}{m_symbol}  {sky}
        Min: {temp_min}{m_symbol}, Max: {temp_max}{m_symbol}

        Wind Speed: {wind_speed}mph, Degree: {wind_degree}
        Humidity: {humidity}
        Cloudiness: {cloudiness}%
        Pressure: {pressure}hPa
        Sunrise at: {sunrise}
        Sunset at: {sunset}

        Last update from the server: {dt}
        ---------------------------------------'''
    return s.format(**data)