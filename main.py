import os
from datetime import date, datetime
import pandas as pd
from table_operations import *
import openpyxl


# initiate empty calendar if it doesn't exist else read xlsx and concat to single DF
if not(os.path.isfile("calendar.xlsx")):
    calendar = create_date_table(start='2024-01-01', end='2024-12-31')
    create_excel_file(calendar)
else:
    calendar = pd.concat(pd.read_excel("calendar.xlsx", engine="openpyxl", sheet_name=None), ignore_index=True)

print(calendar)
# grab today's date and convert to ns64
today = date.today()
today_64 = pd.Timestamp(today).to_datetime64()
print(f"Today is {today}")
print(calendar['Date'].dtype)
print(type(today))
# grab hour to add
got_hour = grab_hour()
write_hour(today_64, calendar, str(got_hour))
create_excel_file(calendar)

