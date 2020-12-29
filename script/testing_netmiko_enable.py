#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
cisco1 = {
    "device_type": "cisco_ios",
    "host": "10.1.255.5",
    "username": "wandy",
    "password": "wandy123",
    "secret" : "wandy123",
}

cisco2 = {
    "device_type": "cisco_ios",
    "host": "10.2.255.112",
    "username": "compnet",
    "password": "C0mpn3t!",
    "secret" : "C0mpn3t!",
}
# Show command that we execute
command1 = "term length 0"
command = "show version"
net_connect = Netmiko(**cisco2)
net_connect.enable()

# output1 = net_connect.send_command_timing(command1, delay_factor=1)
# output = net_connect.send_command_timing(command, delay_factor=1)

output2 = net_connect.send_command(command1)
output3 = net_connect.send_command(command)

# Automatically cleans-up the output so that only the show output is returned
print()
# print(output)
print("No Timing")
print()
print(output3)
net_connect.disconnect()