import json
import urllib2

def load_city_list(data_file):
    with open(data_file, 'r') as city_list:
        data = [json.loads(line) for line in city_list]
        city_list.close()
    return data


def get_city_info(name, data_file='/Users/pjhuang/dev/utils/api_openweathermap/city.list.us.json'):  # need to revise
    # load raw city list file

    try:
        city_list = load_city_list(data_file)
    except IOError as e:
        return 'I/O error({0}): city list file is not does exist. Please double check your path and file name.'.format(
            e.errno)

    # get city information
    city_info = [d for d in city_list if d['name'] == name]
    if len(city_info) == 0:
        print 'The city is not in the API database. Please double check the spelling or use another city name.'
        return None
    elif len(city_info) > 1:
        print 'Duplicated city name. Returning the first one in the list'

    return city_info[0]

print get_city_info('San Francisco')

city_info = get_city_info('San Francisco')

city_id = city_info.get('_id')

user_api = 'c50af3f535984f1f53b97c5bdc514d53'
unit = 'metric'
api_main = 'http://api.openweathermap.org/data/2.5/weather?'

def get_full_api_url(city_name, unit = 'imperial'):
    city_name = city_name.replace(' ', '%20')
    mode = 'json'
#     full_api_url = api_main + 'q=' + city_name + '&units=' + unit + '&mode=' mode + '&appid=' + user_api
    full_api_url = "{}q={}&units={}&mode={}&appid={}".format(api_main, city_name, unit, mode, user_api)
    return full_api_url

print get_full_api_url('San Francisco')

api_url = get_full_api_url('San Francisco')

def get_current_weather(api_url):
    json_file = urllib2.urlopen(api_url)
    api_data = json.load(json_file)
    return api_data

print get_current_weather(api_url)


api_data = get_current_weather(api_url)

def output_data(api_data):
    print '-----------------------------'
    print 'Current weather in: {0}'.format(api_data['name'])
    print api_data['main']['temp'], api_data['weather'][0]['main']
    print 'Max: {}, Min: {}'.format(api_data['main']['temp_max'], api_data['main']['temp_min'])
    print '-----------------------------'
    return None

print output_data(api_data)