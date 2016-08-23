import datetime

def time_converter(time, format = '%b %d, %I:%M %p'):
    '''
     convert time int to specified date time format
    :return: human readable date time style
    '''
    converted_time = datetime.datetime.fromtimestamp(int(time)).strftime(format)
    return converted_time
