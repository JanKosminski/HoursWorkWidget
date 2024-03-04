

def save():
    gui_hour = str(hour_input.get())
    top.write_hour(today_64, calendar, str(gui_hour))


window = tk.Tk()
window.title("Godziny Pracu")
window.config(padx=20, pady=20, bg=WHITE)

# Podaj godzinę
desc = tk.Label(text="Podaj godzinę w formacie HH:MM", bg=WHITE)
hour_input = tk.Entry(width=43)
desc.grid(column=0, row=0, sticky="e")
hour_input.grid(column=0, row=1, columnspan=2, sticky="w")
hour_input.insert(0, "00:00")

# zapisz
save_button = tk.Button(text="Zapisz", bg=WHITE,  width=38)
save_button.grid(column=0, row=3, columnspan=2, sticky="w", command=save)


window.mainloop()