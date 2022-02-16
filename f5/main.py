from netmiko import Netmiko
import csv
import time
 
device_data=[]
with open('devices.csv') as csvfile:
    datas = csv.reader(csvfile, delimiter=';')
    for row in datas:
        device_data.append(row)
 
for i in device_data:
    device = {
        'host' : i[1],
        'username' : i[2],
        'password' : i[3],
        'device_type' : i[4]
    }
    write_file = open("outputs/"+i[0]+".txt", "w")
    netconnect = Netmiko(**device)
    # netconnect.enable()
    list_command = i[4]
    commands = []
    with open('command/'+list_command+'.csv') as csvcommand:
        cmd = csv.reader(csvcommand)
        for i in cmd:
            commands.append(i)
    for i in commands :
        print(i[0])
        if i[0]=='display diagnostic-information' :
            output = netconnect.send_command(
                command_string=i[0],
                expect_string=r"diagnostic",
                strip_prompt=False,
                strip_command=False
            )
 
            output = netconnect.send_command(
                command_string="N",
                expect_string='>',
                strip_prompt=False,
                strip_command=False,
                delay_factor=4
            )
            write_file.write(f"\n{i}\n")
            write_file.write(output)
        else :
            output = netconnect.send_command(i[0])
            write_file.write(f"\n{i}\n")
            write_file.write(output)
 
    netconnect.disconnect()