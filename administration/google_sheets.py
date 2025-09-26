import gspread
import pandas as pd

class GoogleSheet:
    def __init__(self,file_name,document,sheet_name):
        self.gc = gspread.service_account(filename=file_name)
        self.sh = self.gc.open(document)
        self.sheet = self.sh.worksheet(sheet_name)

    def get_last_row_range(self):   
        last_row = len(self.sheet.get_all_values()) + 1
        deta = self.sheet.get_values()
        range_start = f"A{last_row}"
        range_end = f"{chr(ord('A') + len(deta[0]) - 1)}{last_row}"
        return f"{range_start}:{range_end}"
    
    # Lista de diccionarios, diccionario es un registro (key = nombre columna, value = valor en columna )
    def get_all_values(self):
        #self.sheet.get_all_values () # this return a list of list, so the get all records is easier to get values filtering
        return self.sheet.get_all_records() # this return a list of dictioraies so the key is the name column and the value is the value for that particular column
    
    def get_last_row(self):
        rows = self.sheet.get_all_values()
        if rows:
            return rows[-1]  # Última fila con datos (lista de celdas)
        else:
            return None
