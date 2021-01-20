import os
import re
from datetime import datetime

from netoprmgr_dm.device_templates.cisco.cucm import CUCM
from netmiko import Netmiko
from steelscript.steelhead.core import steelhead
from steelscript.common.service import UserAuth
import xlrd

#for i in range(first_sheet.nrows), first_sheet is all device data available
def function_capture(first_sheet,first_sheet_command,capture_path,i):
    #value logcapture
    devicename = ''
    ip = ''
    status = ''
    #device type condition
    conditional_device_type = ''
    if first_sheet.row_values(i)[5] == 'cisco_ap':
        conditional_device_type = 'cisco_ios'
    else:
        conditional_device_type = first_sheet.row_values(i)[5]
    my_device = {
        "host": first_sheet.row_values(i)[1],
        "username": first_sheet.row_values(i)[2],
        "password": first_sheet.row_values(i)[3],
        "secret" : first_sheet.row_values(i)[4],
        "device_type": conditional_device_type,
    }

    #exclude device_type '-'
    if my_device["device_type"] == '-':
        print('Device Not Executed :')
        print(first_sheet.row_values(i)[0]+' '+my_device["host"])

        #value logcapture
        devicename = first_sheet.row_values(i)[0]
        ip = first_sheet.row_values(i)[1]
        status = 'Not Executed'

    elif my_device["device_type"] == 'device_type':
        pass
    else:
        print('Device Executed :')
        print(first_sheet.row_values(i)[0]+' '+my_device["host"])
        #write=open(capture_path+'/'+first_sheet.row_values(i)[0]+'-'+first_sheet.row_values(i)[1]+'.txt','w')
        #adding support for riverbed
        if my_device["device_type"] == 'riverbed':

            try:
                auth = UserAuth(username=my_device["username"], password=my_device["password"])
                sh = steelhead.SteelHead(host=my_device["host"], auth=auth)
                #writing log
                write=open(capture_path+'/'+first_sheet.row_values(i)[0]+'-'+first_sheet.row_values(i)[1]+'.txt','w')
                write.write(first_sheet.row_values(i)[5]+'\n')
                
                #value logcapture
                devicename = first_sheet.row_values(i)[0]
                ip = first_sheet.row_values(i)[1]
                status = 'Executed'

                #show command

                for command in range(first_sheet_command.nrows):
                    if my_device["device_type"] == first_sheet_command.row_values(command)[0]:
                        count_column = 1
                        #while count_column < 8:
                        for cmd in (first_sheet_command.row_values(command,start_colx=0,end_colx=None)):
                            try:
                                output = sh.cli.exec_command(first_sheet_command.row_values(command)[count_column])
                                print(first_sheet_command.row_values(command)[count_column])
                                print(output)
                                write.write(first_sheet_command.row_values(command)[count_column]+'\n')
                                write.write(output+'\n')
                            except:
                                pass
                            count_column+=1
            
            except:
                devicename = first_sheet.row_values(i)[0]
                ip = first_sheet.row_values(i)[1]
                status = 'Cannot Remote Device'
            #tolong dibenerin
            #except NameError:
                #raise
        elif 'ucm_' in my_device["device_type"]:
            try:
                functionCUCM = CUCM(first_sheet,first_sheet_command,capture_path,i)
                devicename = first_sheet.row_values(i)[0]
                ip = first_sheet.row_values(i)[1]
                status = 'Executed'
            except:
                devicename = first_sheet.row_values(i)[0]
                ip = first_sheet.row_values(i)[1]
                status = 'Not Executed'

        else:
            #response = os.system("ping -c 1 " + my_device["host"])
            #if response == 0:
            try:
                net_connect = Netmiko(**my_device)
                try:
                    net_connect.enable()
                except:
                    pass
                #writing log
                write=open(capture_path+'/'+first_sheet.row_values(i)[0]+'-'+first_sheet.row_values(i)[1]+'.txt','w')
                #key information about device
                write.write(first_sheet.row_values(i)[5]+'\n')

                #value logcapture
                devicename = first_sheet.row_values(i)[0]
                ip = first_sheet.row_values(i)[1]
                status = 'Executed'

                #show command

                for command in range(first_sheet_command.nrows):
                    if first_sheet.row_values(i)[5] == first_sheet_command.row_values(command)[0]:
                        count_column = 1
                        #while count_column < 8:
                        for enum, cmd in enumerate(first_sheet_command.row_values(command,start_colx=0,end_colx=None)):
                            try:
                                if 'clear' in first_sheet_command.row_values(command)[count_column]:
                                    output = net_connect.send_command(first_sheet_command.row_values(command)[count_column], expect_string="\[confirm\]")
                                    print(first_sheet_command.row_values(command)[count_column])
                                    print(output)
                                    write.write(first_sheet_command.row_values(command)[count_column]+'\n')
                                    write.write(output+'\n')
                                    output = net_connect.send_command("\n", expect_string="#")
                                    print(output)
                                elif first_sheet_command.row_values(command)[count_column] == '':
                                    break
                                else:
                                    #adding sign
                                    if enum == 10:
                                        sign_day = (datetime.now().day)
                                        sign_month = (datetime.now().month)
                                        sign_year = (datetime.now().year)
                                        sign_year = re.findall('..(..)', str(sign_year))
                                        sign_year = sign_year[0]
                                        sign_ludes = str(f'show{sign_day}clock{sign_year}show{sign_month}time\n')
                                        write.write(sign_ludes)
                                        output = net_connect.send_command(first_sheet_command.row_values(command)[count_column])
                                        print(first_sheet_command.row_values(command)[count_column])
                                        print(output)
                                        write.write(first_sheet_command.row_values(command)[count_column]+'\n')
                                        write.write(output+'\n')
                                    else:
                                        output = net_connect.send_command(first_sheet_command.row_values(command)[count_column])
                                        print(first_sheet_command.row_values(command)[count_column])
                                        print(output)
                                        write.write(first_sheet_command.row_values(command)[count_column]+'\n')
                                        write.write(output+'\n')
                            except:
                                pass
                            count_column+=1

                #disconnect netmiko
                net_connect.disconnect()
            
            except:
                devicename = first_sheet.row_values(i)[0]
                ip = first_sheet.row_values(i)[1]
                status = 'Wrong Username Password'
            #except NameError:
                #raise
            #else:
                #devicename = first_sheet.row_values(i)[0]
                #ip = first_sheet.row_values(i)[1]
                #status = 'Cannot Ping Device'

    #return value log           
    log_device = {
        "devicename" : devicename,
        "ip" : ip,
        "status" : status
    }
    return log_device
