#!/usr/bin/env python

"""
INFO: This script adds connects to multiple Cisco devices, as specified in a
json dictionary file, and gets the serial number from each device.

AUTHOR: zmw

DATE: 20161212 21:55 PST
"""

#Make script compatible with both Python2 and Python3.
from __future__ import absolute_import, division, print_function

#Import functions/libraries needed.
import netmiko
import json
import mytools
import sys
import signal

#Silently exit upon user interruption (eg. Ctrl-C).
signal.signal(signal.SIGPIPE, signal.SIG_DFL) #IOError: Broken Pipe
signal.signal(signal.SIGINT, signal.SIG_DFL) #KeyboardInterrupt: Ctrl-C

#Identifying possible exceptions/errors that may arise.
netmiko_exceptions = (netmiko.ssh_exception.NetMikoAuthenticationException,
                      netmiko.ssh_exception.NetMikoTimeoutException)

#Welcome message printed to screen.
print('='*80)
print('Welcome to the Cisco Serial Numbers Script!')
print('='*80)

#Read in devices/info from a specific json file and run commands.
with open('devices.json') as dev_file:
  devices = json.load(dev_file)

#For loop which cycles through all devices in dev_file specified above.
for device in devices:
  try:
    #Prompt user for their username/password and temporarily add to dictionary.
    print('Login to', device['ip'],'...')
    username, password = mytools.get_credentials()
    device['username'] = username
    device['password'] = password
    #Check if the device_type is cisco_ios, then run the following.
    if device['device_type'] == 'cisco_ios':
      #Connect to device.
      connection = netmiko.ConnectHandler(**device)
      #Run command(s) to get serial number from device and print to screen.
      serialnum = str(connection.send_command('show version | i Processor board ID'))
      serialnum = serialnum[19:]
      print(device['ip'],"Serial Number:", serialnum)
      #Disconnect from device.
      connection.disconnect()
      print('-'*80)
    #Check if the device_type is cisco_xe, then run the following.
    elif device['device_type'] == 'cisco_xe':
      #Connect to device.
      connection = netmiko.ConnectHandler(**device)
      #Run command(s) to get serial number from device and print to screen.
      serialnum = str(connection.send_command('show version | i Processor board ID'))
      serialnum = serialnum[19:]
      print(device['ip'],"Serial Number:", serialnum)
      #Disconnect from device.
      connection.disconnect()
      print('-'*80)
    #Check if the device_type is cisco_xr, then run the following.
    elif device['device_type'] == 'cisco_xr':
      #Connect to device.
      connection = netmiko.ConnectHandler(**device)
      #Run command(s) to get serial number from device and print to screen.
      serialnum = str(connection.send_command('admin show diag chassis | i S/N'))
      serialnum = serialnum[38:]
      print(device['ip'],"Serial Number:", serialnum)
      #Disconnect from device.
      connection.disconnect()
      print('-'*80)
    #If the device type is not cisco_ios, cisco_xe or cisco_xr, give up!
    else:
      print('Sorry, I cannot get the S/N for this device type/OS.')
      print('-'*80)
  #Let user know if script was unable to connect to a device.
  except netmiko_exceptions as e:
    print('Failed to connect to', device['ip'], 'Error:', e)
    print('-'*80)
