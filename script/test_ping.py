import os

hostname0 = "12.10.10.10"

response = os.system("ping -n 1 " + hostname0)

if response == 0:
    print (hostname0, 'is up')
else:
    print (hostname0, 'is down')