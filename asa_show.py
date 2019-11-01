import netmiko
import re
import getpass
from datetime import datetime
import datetime

print ('''
##############################################################################################################
##--------------------------------- Welcome to ASA Configuration Fetcher -----------------------------------##
##----------------------------------------------------------------------------------------------------------##
## You can collect configuration using this Script and use a tool to compare before and after configuration.##
##                                               Version 1.0                                                ##
##############################################################################################################
''')
commands = ['show int ip bri', 'show failover', 'show access-list | i name hash', 'show shun', 'show run all']
print ("""Please create a file consisting the IPs/Names you want this script to run against.
Your output file will be automatically created with the name "timestamp_ASA-output".
Make sure your user has necessary priviledges to create files in the directory you are running this script. \n""")
input_devices_file = input ("Enter your Input Device File Name : ")
user = input ("Enter your username : ")
pw = getpass.getpass("Enter your password : ")
#epw = getpass.getpass("Enter your enable secret : ")
f = open (input_devices_file, "r")
g = open ("%s_ASA-OUTPUT.txt" % datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S") , "a+")
devices = f.read().split("\n")
f.close()
for device in devices:
    print (f'-------- Connecting to {device} ----------')
    print (datetime.datetime.now())
    g.write(f'---------------- Connecting to {device} ------------------\n')
    g.write (str(datetime.datetime.now())+"\n")
    asa = netmiko.ConnectHandler(host=device, username=user, password=pw, device_type="cisco_asa", secret="admin12#$")
    for command in commands:
        print (f'-------- Sending Command {command} ----------')
        g.write(f'-------- Sending Command {command} ----------\n')
        output = asa.send_command(command)
        print (output)
        g.write(output)
g.close()
