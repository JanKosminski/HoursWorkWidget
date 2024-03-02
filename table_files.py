import pandas as pd


def create_date_table(start='2000-01-01', end='2050-12-31'):
    start_ts = pd.to_datetime(start).date()

    end_ts = pd.to_datetime(end).date()

    # record timetsamp is empty for now
    dates = pd.DataFrame(columns=['Entry Hour', 'Leave Hour'], index=pd.date_range(start_ts, end_ts))
    dates.index.name = 'Date'

    days_names = {
        i: name
        for i, name
        in enumerate(['Monday', 'Tuesday', 'Wednesday',
                      'Thursday', 'Friday', 'Saturday',
                      'Sunday'])
    }

    dates['Day'] = dates.index.dayofweek.map(days_names.get)
    dates['Month'] = dates.index.month
    dates.reset_index(inplace=True)
    dates.index.name = 'date_id'
    return dates


def write_to_table(date):
    pass