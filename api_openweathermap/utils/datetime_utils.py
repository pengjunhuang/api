import datetime
import pytz

def time_converter(time, date_format='%b %d, %I:%M %p', timezone='America/Los_Angeles', offset=0):
    """
    convert time int to specified date time format

    :param time  UNIX time
    :param date_format date format to display
    :param timezone time zone default is America/Los_Angeles
    :param offset optional, used when user does not know the timezone and need to adjust time manually
    :return: human readable date time style
    """

    converted_time = datetime.datetime.fromtimestamp(int(time) + offset * 3600, pytz.timezone(timezone)).strftime(date_format)
    return converted_time
