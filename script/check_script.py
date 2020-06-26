import os
import re

current_dir=os.getcwd()
files = os.listdir(current_dir)
count_file = 0
for file in files:
    if 'check_script' in file:
        pass
    else:
        try:
            read_file = open(file, 'r')
            read_file_list = read_file.readlines()
            for line in read_file_list:
                #if "PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process" in line:
                if re.findall('^hostname (.*)', line):
                    regex = re.findall('^hostname (.*)', line)
                    print(file+';'+regex[0])
                    count_file+=1
                    break
        except:
            pass
print('Total File : '+str(count_file))

'''
current_dir=os.getcwd()
files = os.listdir(current_dir)
count_file = 0
for file in files:
    if '__pycache__' in file:
        pass
    elif 'check_script.py' in file:
        pass
    elif '__init__.py' in file:
        pass
    elif 'cisco_None.py' in file:
        pass
    else:
        print(file)
        count_file+=1
print('Total File : '+str(count_file))
'''