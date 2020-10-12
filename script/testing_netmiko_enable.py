#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
cisco1 = {
    "device_type": "cisco_ios",
    "host": "10.103.1.36",
    "username": "cakra",
    "password": "s0n1cm4st3r",
    "secret" : "adminmor3",
}
# Show command that we execute
command = "show running-config"
net_connect = Netmiko(**cisco1)
net_connect.enable()
output = net_connect.send_command(command)
# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print()
net_connect.disconnect()