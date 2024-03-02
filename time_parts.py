from datetime import date, datetime


def grab_hour():
    hour = input("Enter work entry hour in HH:MM format please: ")
    stripped_hour = datetime.strptime(f"{hour}:00", "%H:%M:%S")
    return stripped_hour

def time_diff():

entry = grab_hour()


leave_hour = input("Enter the hour you left the work in HH:MM format please: ")
end_time = datetime.strptime(f"{leave_hour}:00", "%H:%M:%S")

# get difference
delta = end_time - start_time
worked_sec = delta.total_seconds()
worked_hours = (worked_sec - (worked_sec % 3600)) / 3600
worked_hours_float = worked_sec / 3660
print(f"Total time worked is {worked_hours}:{(worked_sec % 3600)/60}")
