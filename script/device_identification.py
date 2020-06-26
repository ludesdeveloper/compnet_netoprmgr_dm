#using netmiko without raw_data include device_type
import xlrd
import xlsxwriter
from netmiko import Netmiko

def device_identification(raw_data_dir):
    book = xlrd.open_workbook(raw_data_dir)
    first_sheet = book.sheet_by_index(0)
    cell = first_sheet.cell(0,0)

    wb = xlsxwriter.Workbook('devices_data.xlsx')
    ws = wb.add_worksheet('summary')

    suported_device = ['cisco_ios','cisco_xr','cisco_asa','cisco_nxos','cisco_xe']
    count_row = 0

    for i in range(first_sheet.nrows):
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

                ws.write(count_row,0,first_sheet.row_values(i)[0])
                ws.write(count_row,1,my_device["host"])
                ws.write(count_row,2,my_device["username"])
                ws.write(count_row,3,my_device["password"])
                ws.write(count_row,4,my_device["secret"])
                #harus di cari device typenya
                #ws.write(count_row,4,my_device["device_type"])


                if 'Cisco Adaptive Security Appliance Software' in output:                                                   
                    ws.write(count_row,5,'cisco_asa')

                elif 'Cisco IOS XE Software' in output:                                                    
                    ws.write(count_row,5,'cisco_xe')

                elif 'Cisco IOS Software' in output:
                    ws.write(count_row,5,'cisco_ios')                           
                    
                elif 'Cisco Nexus Operating System (NX-OS) Software' in output:                         
                    ws.write(count_row,5,'cisco_nxos')                          
                    
                elif 'Cisco Controller' in output:                         
                    ws.write(count_row,5,'cisco_wlc')
                
                else:
                    ws.write(count_row,5,'unidentified')

                break
            
            #except NameError:
                #raise
            except:
                #pass
                my_device = {
                    "host": first_sheet.row_values(i)[1],
                    "username": first_sheet.row_values(i)[2],
                    "password": first_sheet.row_values(i)[3],
                    "secret" : first_sheet.row_values(i)[4],
                    "device_type": j,
                }

                ws.write(count_row,0,first_sheet.row_values(i)[0])
                ws.write(count_row,1,my_device["host"])
                ws.write(count_row,2,my_device["username"])
                ws.write(count_row,3,my_device["password"])
                ws.write(count_row,4,my_device["secret"])
                ws.write(count_row,5,'-')
                
        count_row+=1
    wb.close()