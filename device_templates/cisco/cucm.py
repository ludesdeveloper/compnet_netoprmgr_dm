import paramiko
import re
from paramiko_expect import SSHClientInteraction

def CUCM(capture_path):
    #Set Connection and Credentials
    host=('172.22.200.211')
    user=('admin')
    pwd=('iTM@#2012')

    #SSH to client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=pwd)
    interact = SSHClientInteraction(ssh, timeout=60, display=True)
    interact.expect('admin:')
    interact.send('set cli pagination off')
    interact.expect('admin:')

    #Command capture
    cucm_commands = ['show network cluster', 'show hardware', 'show network eth0', 'show version active', 'show status', 'show network ipprefs all', 'utils ntp status', 
    'show process load cpu', 'show process load memory', 'utils disaster_recovery history backup', 'utils dbreplication runtimestate', 'show risdb query phone', 
    'file tail activelog /cm/log/amc/AlertLog/AlertLog_11_03_2020_09_36.csv 30']
    write = open(capture_path+'/cucm.txt','w')
    for cucm_command in cucm_commands:

        interact.send(cucm_command)
        interact.expect('admin:')
        output = interact.current_output_clean
        write.write(cucm_command + '\n')
        write.write(output)

    #Command to list certificate
    interact.send('show cert list own')
    interact.expect('admin:')
    output = interact.current_output_clean
    output = output.splitlines()
    # write = open('cucm_certs.txt','w')

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