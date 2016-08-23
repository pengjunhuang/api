import datetime
import pytz

def time_converter(time, format = '%b %d, %I:%M %p'):
    '''
     convert time int to specified date time format
    :return: human readable date time style
    '''
    # TODO: remove Hardcoded Timezone
    converted_time = datetime.datetime.fromtimestamp(int(time), pytz.timezone('America/Los_Angeles')).strftime(format)
    return converted_time
