import openpyxl
wb=openpyxl.load_workbook('example.xlsx')
#ws=wb.active
ws=wb["Sheet1"]
wb.create_sheet('NewSheet1', 0)