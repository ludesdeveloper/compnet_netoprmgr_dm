from netmiko import Netmiko

my_device = {
    "host": '10.206.56.81',
    "username": 'noc.hardi',
    "password": 'Gundam789',
    "device_type": 'cisco_ios',
    "timeout" : 10,
    }

net_connect = Netmiko(**my_device)
#output = net_connect.send_command('show sysinfo')
output = net_connect.send_command('show ver')
print(output)
