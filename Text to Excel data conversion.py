
import openpyxl
from openpyxl import Workbook

# create workbook instance
wb=Workbook()

# sheet name update
wb['Sheet'].title="List_Of_City"
sh1=wb.active

#read txt data from Source file
with open("full_list_city","r") as f:
    for line in f:
#        row_data = f.readline().split(";")
        #Converting data into List using list and specifying the delimiter
        row_data = line.split(";")
        #row_data = row_data.split(";")
        sh1.append(row_data)
        print(row_data)

#save the workbook
wb.save("Excel_Full_City.xlsx")

