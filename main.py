import os
from datetime import date, datetime


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