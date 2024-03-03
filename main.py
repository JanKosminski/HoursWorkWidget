import os
from datetime import date, datetime
import pandas as pd
from table_files import *
import openpyxl
import calendar

months_list = [calendar.month_name[i] for i in range(1, 13)]
# grab today's date
today = date.today()
print(f"Today is {today}")

# grab today's entry time
# TODO - add GUI
entry_hour = input("Enter work entry hour in HH:MM format please: ")
leave_hour = input("Enter the hour you left the work in HH:MM format please: ")
start_time = datetime.strptime(f"{entry_hour}:00", "%H:%M:%S")
end_time = datetime.strptime(f"{leave_hour}:00", "%H:%M:%S")

# get difference
delta = end_time - start_time
worked_sec = delta.total_seconds()
worked_hours = (worked_sec - (worked_sec % 3600)) / 3600
worked_hours_float = worked_sec / 3660
print(f"Total time worked is {worked_hours}:{(worked_sec % 3600)/60}")


# initiate calendar if it doesn't exist else read to DF

if not(os.path.isfile("calendar.xlsx")):
    calendar = create_date_table(start='2024-01-01', end='2024-12-31')
    with pd.ExcelWriter('calendar.xlsx') as writer:
        for i, j in enumerate(months_list):
            page = calendar.loc[calendar['Month'] == (i+1)]
            page.to_excel(writer, sheet_name=str(j))
else:
    calendar = pd.read_excel("calendar.xlsx", engine="openpyxl")

print(calendar)