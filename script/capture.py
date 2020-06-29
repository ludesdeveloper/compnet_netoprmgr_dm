import os
import re

from netmiko import Netmiko
from steelscript.steelhead.core import steelhead
from steelscript.common.service import UserAuth
import xlrd

def function_capture(first_sheet,first_sheet_command,capture_path,i):

    
    my_device = {
        "host": first_sheet.row_values(i)[1],
        "username": first_sheet.row_values(i)[2],
        "password": first_sheet.row_values(i)[3],
        "secret" : first_sheet.row_values(i)[4],
        "device_type": first_sheet.row_values(i)[5],
    }
    print('Device Executed :')
    print(first_sheet.row_values(i)[0]+' '+my_device["host"])
    write=open(capture_path+'/'+first_sheet.row_values(i)[0]+'-'+first_sheet.row_values(i)[1]+'.txt','w')
    #adding support for riverbed
    if my_device["device_type"] == 'riverbed':

        try:
            auth = UserAuth(username=my_device["username"], password=my_device["password"])
            sh = steelhead.SteelHead(host=my_device["host"], auth=auth)
            write.write(first_sheet.row_values(i)[5]+'\n')

            #show command

            for command in range(first_sheet_command.nrows):
                if my_device["device_type"] in first_sheet_command.row_values(command)[0]:
                    count_column = 1
                    #while count_column < 8:
                    for cmd in (first_sheet_command.row_values(command,start_colx=0,end_colx=None)):
                        try:
                            output = sh.cli.exec_command(first_sheet_command.row_values(command)[count_column])
                            print(first_sheet_command.row_values(command)[count_column])
                            print(output)
                            write.write(first_sheet_command.row_values(command)[count_column]+'\n')
                            write.write(output+'\n')
                            count_column+=1
                        except:
                            pass
        
        except:
            write.write('Cannot Remote Device')
        #except NameError:
            #raise
    else:
        try:
            net_connect = Netmiko(**my_device)
            #key information about device
            write.write(first_sheet.row_values(i)[5]+'\n')

            #show command

            for command in range(first_sheet_command.nrows):
                if my_device["device_type"] in first_sheet_command.row_values(command)[0]:
                    count_column = 1
                    #while count_column < 8:
                    for cmd in (first_sheet_command.row_values(command,start_colx=0,end_colx=None)):
                        try:
                            output = net_connect.send_command(first_sheet_command.row_values(command)[count_column])
                            print(first_sheet_command.row_values(command)[count_column])
                            print(output)
                            write.write(first_sheet_command.row_values(command)[count_column]+'\n')
                            write.write(output+'\n')
                            count_column+=1
                        except:
                            pass

            #disconnect netmiko
            net_connect.disconnect()
        
        except:
            write.write('Cannot Remote Device')
        #except NameError:
            #raise
