import os

from netmiko import Netmiko
import xlrd
import xlsxwriter
import shutil

def function_check(data_dir,capture_path):

    book = xlrd.open_workbook(data_dir)
    first_sheet = book.sheet_by_index(0)
    cell = first_sheet.cell(0,0)

    wb = xlsxwriter.Workbook('device_availability_check.xlsx')
    ws = wb.add_worksheet('summary')
    ws.write(0,0,'Hostname')
    ws.write(0,1,'IP Address')
    ws.write(0,2,'Status')
    ws.write(0,3,'Authentication')
    count_row=1
    for i in range(first_sheet.nrows):
        host=first_sheet.row_values(i)[1]
        my_device = {
            "host": first_sheet.row_values(i)[1],
            "username": first_sheet.row_values(i)[2],
            "password": first_sheet.row_values(i)[3],
            "device_type": first_sheet.row_values(i)[4],
        }
        response = os.system("ping -n 1 " + host)
    
        if response == 0:
            ws.write(count_row,0,first_sheet.row_values(i)[0])
            ws.write(count_row,1,host)
            ws.write(count_row,2,'Up')
            try:
                net_connect = Netmiko(**my_device)
                ws.write(count_row,3,'Valid')
            except:
                ws.write(count_row,3,'Not Valid')
        else:
            print (host, 'is down')
            ws.write(count_row,0,first_sheet.row_values(i)[0])
            ws.write(count_row,1,host)
            ws.write(count_row,2,'Down')
            ws.write(count_row,3,'-')
        count_row+=1
    wb.close()