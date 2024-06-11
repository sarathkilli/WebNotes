import datetime
def custom_date(date):
    '''
        Convert a datetime into custom format like: Sep 12,2017 19:07:32
    '''
    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    return date.strftime('%b %d,%Y %H:%M:%S')
