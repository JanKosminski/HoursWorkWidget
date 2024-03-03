import os
from datetime import date
import pandas as pd
import table_operations as top
import openpyxl


# initiate empty calendar if it doesn't exist, else read .xlsx and concat to single DF
if not(os.path.isfile("calendar.xlsx")):
    calendar = top.create_date_table(start='2024-01-01', end='2024-12-31')
    top.create_excel_file(calendar)
else:
    calendar = pd.concat(pd.read_excel("calendar.xlsx", engine="openpyxl", sheet_name=None), ignore_index=True)

# grab today's date and convert to ns64
today = date.today()
print(today)
today_64 = pd.Timestamp(today).to_datetime64()
top.sum_hours(today, calendar)
# grab hour to add
# got_hour = top.grab_hour()
# top.write_hour(today_64, calendar, str(got_hour))
# top.create_excel_file(calendar)
