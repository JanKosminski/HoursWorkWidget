import pandas as pd

calendar = pd.concat(pd.read_excel("calendar.xlsx", engine="openpyxl", sheet_name=None), ignore_index=True)
calendar.to_csv("text.csv")