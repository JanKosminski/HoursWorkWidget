import os
from datetime import date
import pandas as pd
import openpyxl
import tkinter as tk
import table_operations as top

WHITE = "#ffffff"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


def save():
    gui_hour = top.grab_hour(str(hour_input.get()))
    top.write_hour(today_64, calendar, str(gui_hour))
    top.create_excel_file(calendar)


# initiate empty calendar if it doesn't exist, else read .xlsx and concat to single DF
if not(os.path.isfile("calendar.xlsx")):
    calendar = top.create_date_table(start='2024-01-01', end='2024-12-31')
    top.create_excel_file(calendar)
else:
    calendar = pd.concat(pd.read_excel("calendar.xlsx", engine="openpyxl", sheet_name=None), ignore_index=True)

# grab today's date and convert to ns64
today = date.today()
today_64 = pd.Timestamp(today).to_datetime64()
top.sum_hours(today, calendar)

window = tk.Tk()
window.title("Godziny Pracy")
window.config(padx=20, pady=20, bg=WHITE)

# Podaj godzinę
desc = tk.Label(text="Podaj godzinę w formacie HH:MM", bg=WHITE)
hour_input = tk.Entry(width=43)
desc.grid(column=0, row=0, sticky="e")
hour_input.grid(column=0, row=1, columnspan=2, sticky="w")
hour_input.insert(0, "00:00")

# zapisz
save_button = tk.Button(text="Zapisz", bg=WHITE, command=save, width=38)
save_button.grid(column=0, row=3, columnspan=2, sticky="w",)

window.mainloop()

