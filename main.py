import os
import time
from datetime import date, datetime
# grab today's date
today = date.today()
print(f"Today is {today}")

# grab today's entry time
entry_hour = input("Enter work entry hour in HH:MM format please: ")
leave_hour = input("Enter the hour you left the work in HH:MM format please: ")
start_time = datetime.strptime(f"{entry_hour}:00", "%H:%M:%S")
end_time = datetime.strptime(f"{leave_hour}:00", "%H:%M:%S")

# get difference
delta = end_time - start_time

sec = delta.total_seconds()
print('difference in seconds:', sec)

min = sec / 60
print('difference in minutes:', min)

# get difference in hours
hours = (min - (min % 60)) / 60
print('difference in hours:', hours)

print(f"Total time worked is {hours}:{min % 60}")