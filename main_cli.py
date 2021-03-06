import os
import time
import re
import pkg_resources
import shutil
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor
import xlrd
import xlsxwriter
from zipfile import ZipFile

from netoprmgr_dm.script.capture import function_capture
from netoprmgr_dm.script.check import function_check
from netoprmgr_dm.script.device_identification import device_identification
from netoprmgr_dm.script.create_template import create_data_template

base_path = pkg_resources.resource_filename('netoprmgr_dm', '')
capture_path = pkg_resources.resource_filename('netoprmgr_dm', 'static/')
capture_path = os.path.join(capture_path,'capture/')
data_path = pkg_resources.resource_filename('netoprmgr_dm', 'static/')
data_path = os.path.join(data_path,'data/')
result_path = pkg_resources.resource_filename('netoprmgr_dm', 'static/')
result_path = os.path.join(result_path,'result/')


class MainCli:

    def deviceIdentification():
        list_devices = []
        chg_dir = os.chdir(data_path)
        current_dir=os.getcwd()
        raw_data_dir = (data_path+'/raw_data.xlsx')
        book = xlrd.open_workbook(raw_data_dir)
        first_sheet = book.sheet_by_index(0)
        cell = first_sheet.cell(0,0)
        suported_device = ['cisco_ios','cisco_xr','cisco_asa','cisco_nxos','cisco_xe']
        count_row = 0
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(device_identification, first_sheet, suported_device, i) for i in range(first_sheet.nrows)]
            print(futures)
            for future in futures:
                try:
                    #print (future.result())
                    list_devices.append(future.result())
                except TypeError as e:
                    print (e)  

        wb = xlsxwriter.Workbook('devices_data.xlsx')
        ws = wb.add_worksheet('summary')
        for enum, device in enumerate(list_devices):
            ws.write(enum,0,device["hostname"])
            ws.write(enum,1,device["ipaddress"])
            ws.write(enum,2,device["username"])
            ws.write(enum,3,device["password"])
            ws.write(enum,4,device["secret"])
            ws.write(enum,5,device["device_type"])
        wb.close()
        #call_device_identification = device_identification(raw_data_dir)

    def deviceAvailability():
        chg_dir = os.chdir(capture_path)
        current_dir=os.getcwd()
        data_dir = (data_path+'/devices_data.xlsx')
        call_function_check=function_check(data_dir,capture_path)
        src_mv = (capture_path+'device_availability_check.xlsx')
        dst_mv = (result_path+'device_availability_check.xlsx')
        shutil.move(src_mv,dst_mv)

    def captureDevice():
        chg_dir = os.chdir(capture_path)
        current_dir=os.getcwd()
        files = os.listdir(current_dir)
        for file in files:
            if file.endswith(".zip"):
                os.remove(file)
        data_dir = (data_path+'/devices_data.xlsx')
        command_dir = (data_path+'/show_command.xlsx')
        #start multi thread
        book = xlrd.open_workbook(data_dir)
        first_sheet = book.sheet_by_index(0)
        cell = first_sheet.cell(0,0)

        book_command = xlrd.open_workbook(command_dir)
        first_sheet_command = book_command.sheet_by_index(0)
        cell_command = first_sheet_command.cell(0,0)
        
        list_log = []

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(function_capture, first_sheet, first_sheet_command, capture_path, i) for i in range(first_sheet.nrows)]
            print(futures)
            for future in futures:
                try:
                    #print (future.result())
                    if future.result()['devicename'] == '':
                        pass
                    else:
                        list_log.append(future.result())
                except TypeError as e:
                    print (e)
        
        #write logcapture.txt
        print ('list_log')
        print (list_log)
        write = open('logcapture.txt', 'w')
        for log in list_log:
            write.write(log['devicename']+' | '+log['ip']+' | '+log['status']+'\n')
        write.close()

        chg_dir = os.chdir(capture_path)
        current_dir=os.getcwd()
        files = os.listdir(current_dir)
        zipObj = ZipFile('captures.zip', 'w')
        for file in files:
            if '__init__.py' in file:
                pass
            else:
                zipObj.write(file)
        zipObj.close()

    def createTemplate():
        chg_dir = os.chdir(data_path)
        function_create_data_template=create_data_template()

    def deleteCapture():
        chg_dir = os.chdir(capture_path)
        current_dir=os.getcwd()
        files = os.listdir(current_dir)
        for file in files:
            if '__init__.py' in file:
                pass
            else:
                try:
                    os.remove(file)
                    print('Deleting '+str(file))
                except:
                    pass

if __name__ == "__main__":
    answer=input(
    'Type "template" to create template on data folder\n\n'
    'Press Number for MENU :\n'
    '1. Device Identification (Still Development)\n'
    '2. Device Availability Check\n'
    '3. Capture\n'
    'Type "quit" to quit program\n'
    )
    if answer == '1':
        MainCli.deviceIdentification()
    elif answer == '2':
        MainCli.deviceAvailability()
    elif answer == '3':
        MainCli.captureDevice()
    elif answer == 'template':
        MainCli.createTemplate()