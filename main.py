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


def sum_gui():
    a = variable.get()
    tekst_godzin = top.sum_hours(a, calendar)
    sumed_hours["text"] = f"Suma godzin: {tekst_godzin}  -- skopiowano do schowka"
    window.clipboard_clear()
    window.clipboard_append(tekst_godzin)


month = 0
# initiate empty calendar if it doesn't exist, else read .xlsx and concat to single DF

if not (os.path.isfile("calendar.xlsx")):
    calendar = top.create_date_table(start='2024-01-01', end='2024-12-31')
    top.create_excel_file(calendar)
else:
    calendar = pd.concat(pd.read_excel("calendar.xlsx", engine="openpyxl", sheet_name=None), ignore_index=True)

# grab today's date and convert to ns64
today = date.today()
today_64 = pd.Timestamp(today).to_datetime64()

# GUI
window = tk.Tk()
window.title("Godziny Pracy")
window.config(padx=20, pady=20, bg=WHITE)

# Podaj godzinę
desc = tk.Label(text="Podaj godzinę w formacie HH:MM", bg=WHITE)
hour_input = tk.Entry(width=28)
desc.grid(column=0, row=0, sticky="w", columnspan=2)
hour_input.grid(column=0, row=1, sticky="w")
hour_input.insert(0, "00:00")

# zapisz
save_button = tk.Button(text="Zapisz", bg=WHITE, command=save, width=10)
save_button.grid(column=1, row=1, sticky="e",)

# sumuj godziny
save_button = tk.Button(text="Sumuj godziny", bg=WHITE, command=sum_gui, width=38)
save_button.grid(column=0, row=4, columnspan=2, sticky="w")

# godziny
sumed_hours = tk.Label(text="Suma godzin: ", bg=WHITE)
sumed_hours.grid(column=0, row=5, columnspan=2, sticky="w")

# opis listy
desc2 = tk.Label(text="Wybierz numer miesiąca", bg=WHITE)
desc2 .grid(column=0, row=6, columnspan=2, sticky="w")
# lista
month_numbers = [i for i in range(1, 13)]

variable = tk.StringVar(window)
variable.set(month_numbers[0])
# default value
w = tk.OptionMenu(window, variable, *month_numbers)
w.grid(column=1, row=6, columnspan=2, sticky="e")
window.mainloop()
