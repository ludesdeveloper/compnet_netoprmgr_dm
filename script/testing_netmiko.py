#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

cisco1 = {
    "device_type": "cisco_ios",
    "host": "cisco1.lasthop.io",
    "username": "username",
    "password": "password",
}

# Show command that we execute
command = "show inventory"
with Netmiko(**cisco1) as net_connect:
    output = net_connect.send_command(command)

# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print()