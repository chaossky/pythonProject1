# ÆÄÀÌ½ã ¿¢¼¿ ÆÄÀÏ »ý¼º
from webbrowser import get
import openpyxl

filepath="test.xlsx"
wb=openpyxl.Workbook()
wb.save(filepath)

# excelFime=openpyxl.load_workbook('example.xlsx')
# sheet=wb.active

# sheet=wb["sheet1"]

# get_sheet_names()
# excelFime.get_sheet_names()

# sheet1=excelFile.get_sheet_by_name('sheet1')

# sheet2=excelFile.get_sheet_by_name('sheet2')
