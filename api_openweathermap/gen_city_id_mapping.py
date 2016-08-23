#!/Users/pjhuang/anaconda/bin python
'''
This script is used to retrieve the city IDs list from the OWM web 2.5 API
'''
import json


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

