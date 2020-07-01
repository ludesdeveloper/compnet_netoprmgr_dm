import os
import time
import re
import pkg_resources
import shutil
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor
import xlrd
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
        chg_dir = os.chdir(data_path)
        current_dir=os.getcwd()
        raw_data_dir = (data_path+'/raw_data.xlsx')
        call_device_identification = device_identification(raw_data_dir)

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
        '''
        jobs = []

        for i in range(first_sheet.nrows):
            #call_function_capture=function_capture(first_sheet,first_sheet_command,capture_path)
            my_thread = threading.Thread(target=function_capture, args=(first_sheet,first_sheet_command,capture_path,i))
            jobs.append(my_thread)

        for job in jobs:
            job.start()

        for job in jobs:
            job.join()
        '''
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(function_capture, first_sheet, first_sheet_command, capture_path, i) for i in range(first_sheet.nrows)]
            print(futures)
            for future in futures:
                try:
                    print (future.result())
                except TypeError as e:
                    print (e)   
        
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