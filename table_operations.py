import pandas as pd
import calendar
from datetime import datetime
import numpy as np

months_list = [calendar.month_name[i] for i in range(1, 13)]


def create_date_table(start='2000-01-01', end='2050-12-31'):
    start_ts = pd.to_datetime(start).date()
    end_ts = pd.to_datetime(end).date()
    # record timestamp is empty for now
    dates = pd.DataFrame(columns=['Entry Hour', 'Leave Hour', 'Time Spent Working'],
                         index=pd.date_range(start_ts, end_ts))
    dates.index.name = 'Date'
    days_names = {
        i: name
        for i, name in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    }
    dates['Day'] = dates.index.dayofweek.map(days_names.get)
    dates['Month'] = dates.index.month
    dates.reset_index(inplace=True)
    dates.index.name = 'date_id'
    return dates


def write_hour(date, dataframe, hour):
    index = dataframe.isin([date]).any(axis=1).idxmax()
    if pd.isna(dataframe.loc[index, 'Entry Hour']):
        dataframe._set_value(index, 'Entry Hour', hour)
    else:
        dataframe._set_value(index, 'Leave Hour', hour)
        dataframe[['Entry Hour', 'Leave Hour']] = dataframe[['Entry Hour', 'Leave Hour']].apply(pd.to_datetime)
        dataframe['Time Spent Working'] = dataframe['Time Spent Working'].astype(object)
        diff_sec = pd.Timedelta(dataframe.iloc[index]['Leave Hour'] - dataframe.iloc[index]['Entry Hour']).seconds
        diff = f"{int((diff_sec - diff_sec % 3600)/ 3600.0)}:{int((diff_sec % 3600)/60)}"
        dataframe._set_value(index, 'Time Spent Working', diff)


def create_excel_file(dataframe):
    with pd.ExcelWriter('calendar.xlsx') as writer:
        for i, j in enumerate(months_list, start=1):
            page = dataframe.loc[dataframe['Month'] == i]
            page.to_excel(writer, sheet_name=j)


def grab_hour():
    hour = input("Enter hour in HH:MM format please: ")
    stripped_hour = datetime.strptime(f"{hour}:00", "%H:%M:%S")
    return stripped_hour
