import json
import urllib2


def get_api_data(url):
    """
    :param url, api url
    :return: a dictionary / json format data contains api data
    """
    json_file = urllib2.urlopen(url)
    api_data = json.load(json_file)
    return api_data
