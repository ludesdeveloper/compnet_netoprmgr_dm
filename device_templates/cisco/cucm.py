import paramiko
import re
from paramiko_expect import SSHClientInteraction

def CUCM(first_sheet,first_sheet_command,capture_path,i):
    #Set Connection and Credentials
    my_device = {
        "host": first_sheet.row_values(i)[1],
        "username": first_sheet.row_values(i)[2],
        "password": first_sheet.row_values(i)[3],
        "secret" : first_sheet.row_values(i)[4],
        "device_type": first_sheet.row_values(i)[5],
    }
    # myhost = my_device['host']
    # myusername = my_device['username']
    # mypassword = my_device['password']

    host=my_device["host"]
    user=my_device["username"]
    pwd=my_device["password"]

    #SSH to client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=pwd)
    interact = SSHClientInteraction(ssh, timeout=60, display=True)
    interact.expect('admin:')
    interact.send('set cli pagination off')
    interact.expect('admin:')

    #Command capture
    # cucm_commands = ['show network cluster', 'show hardware', 'show network eth0', 'show version active', 'show status', 'show network ipprefs all', 'utils ntp status', 
    # 'show process load cpu', 'show process load memory', 'utils disaster_recovery history backup', 'utils dbreplication runtimestate', 'show risdb query phone', 
    # 'file tail activelog /cm/log/amc/AlertLog/AlertLog_11_03_2020_09_36.csv 30']
    write=open(capture_path+'/'+first_sheet.row_values(i)[0]+'-'+first_sheet.row_values(i)[1]+'.txt','w')


    for command in range(first_sheet_command.nrows):
        if my_device["device_type"] in first_sheet_command.row_values(command)[0]:
            count_column = 1
            #while count_column < 8:
            for cmd in (first_sheet_command.row_values(command,start_colx=0,end_colx=None)):
                try:
                    if (first_sheet_command.row_values(command)[count_column]) == '' :
                        break
                    else:
                        interact.send(first_sheet_command.row_values(command)[count_column])
                        interact.expect('admin:')
                        output = interact.current_output_clean
                        write.write(first_sheet_command.row_values(command)[count_column]+'\n')
                        write.write(output)
                except:
                    pass

                count_column+=1

    #Command to list certificate
    interact.send('show cert list own')
    interact.expect('admin:')
    output = interact.current_output_clean
    output = output.splitlines()

    #Print certificate
    for i in output:
        if i == '':
            pass
        else:
            cert_regex = re.findall('(.*):', i)
            cert_regex = cert_regex[0]
            interact.send('show cert own ' + cert_regex)
            interact.expect('admin:')
            output = interact.current_output_clean
            # validity_from_regex = re.findall('From:\s+(.*)', output)
            # validity_from_regex = validity_from_regex[0]
            # validity_to_regex = re.findall('To:\s+(.*)', output)
            # validity_to_regex = validity_to_regex[0]
            write.write(cert_regex + '\n')
            write.write(output)
    
    ssh.close()