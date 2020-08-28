#using netmiko without raw_data include device_type
import xlrd
import xlsxwriter
from netmiko import Netmiko

def device_identification(first_sheet, suported_device, i):
    add_device = {}
    if first_sheet.row_values(i)[0] == 'hostname':
        add_device = {
                    "hostname" : "hostname",
                    "ipaddress": "ip address",
                    "username": "username",
                    "password": "password",
                    "secret" : "secret",
                    "device_type": "device_type",
                }
    else:
        print('Executing Device :')
        print(first_sheet.row_values(i)[0])
        for j in suported_device:

            try:

                my_device = {
                    "host": first_sheet.row_values(i)[1],
                    "username": first_sheet.row_values(i)[2],
                    "password": first_sheet.row_values(i)[3],
                    "secret" : first_sheet.row_values(i)[4],
                    "device_type": j,
                    "timeout" : 10,
                }

                net_connect = Netmiko(**my_device)
                '''
                output = net_connect.send_command('show ver')
                if 'Incorrect' in output:
                    output = net_connect.send_command('show sysinfo')
                '''
                print(j)
                if j == 'cisco_wlc':
                    print('show sysinfo')
                    output = net_connect.send_command('show sysinfo')
                else:
                    print('show ver')
                    output = net_connect.send_command('show ver')
                print(output)

                #ws.write(count_row,0,first_sheet.row_values(i)[0])
                #ws.write(count_row,1,my_device["host"])
                #ws.write(count_row,2,my_device["username"])
                #ws.write(count_row,3,my_device["password"])
                #ws.write(count_row,4,my_device["secret"])
                check_device_type = ''
                if 'Cisco Adaptive Security Appliance Software' in output:
                    check_device_type = 'cisco_asa'                                                   
                    #ws.write(count_row,5,'cisco_asa')

                elif 'Cisco IOS XE Software' in output:  
                    check_device_type = 'cisco_xe'                                                   
                    #ws.write(count_row,5,'cisco_xe')

                elif 'Cisco IOS Software' in output:
                    check_device_type = 'cisco_ios'  
                    #ws.write(count_row,5,'cisco_ios')                           
                    
                elif 'Cisco Nexus Operating System (NX-OS) Software' in output:
                    check_device_type = 'cisco_nxos'                          
                    #ws.write(count_row,5,'cisco_nxos')                          
                    
                elif 'Cisco Controller' in output:
                    check_device_type = 'cisco_wlc'                          
                    #ws.write(count_row,5,'cisco_wlc')
                
                elif 'Active-image:' in output:
                    check_device_type = 'cisco_ios'

                elif 'Cisco Sx220 Series Switch Software' in output:
                    check_device_type = 'cisco_ios'

                else:
                    check_device_type = 'unidentified'  
                    #ws.write(count_row,5,'unidentified')
                add_device = {
                    "hostname" : first_sheet.row_values(i)[0],
                    "ipaddress": my_device["host"],
                    "username": my_device["username"],
                    "password": my_device["password"],
                    "secret" : my_device["secret"],
                    "device_type": check_device_type,
                }
                break
            
            #except NameError:
                #raise
            except:
                
                my_device = {
                    "host": first_sheet.row_values(i)[1],
                    "username": first_sheet.row_values(i)[2],
                    "password": first_sheet.row_values(i)[3],
                    "secret" : first_sheet.row_values(i)[4],
                    "device_type": j,
                }
                
                add_device = {
                    "hostname" : first_sheet.row_values(i)[0],
                    "ipaddress": my_device["host"],
                    "username": my_device["username"],
                    "password": my_device["password"],
                    "secret" : my_device["secret"],
                    "device_type": '-',
                }
                
    return add_device