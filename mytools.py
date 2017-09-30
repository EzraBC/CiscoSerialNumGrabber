#!/usr/bin/env python

"""
INFO: This script contains functions for both getting input from a user, as
well as a special function for handling credentials (usernames/passwords) in a
secure and user-friendly way.

AUTHOR: zmw

DATE: 20170108 21:13 PST
"""

#Make script compatible with both Python2 and Python3.
from __future__ import absolute_import, division, print_function

#Import funtion to get password without echoing to screen.
from getpass import getpass

#Make input function compatible with both Python2 and Python3.
def get_input(prompt=''):
	try:
		line = raw_input(prompt)
	except NameError:
		line = input(prompt)
	return line

#Use one of the following 3 options to get username and password
#(uncomment to use)

#Preset username and password.
def get_credentials():
    username = "your-username"
    password = "your-password"
    return username, password

#Prompt for username once and password once, return both.
# def get_credentials():
#	username = get_input('   Enter Username: ')
#	password = getpass('   Enter RSA PASSCODE: ')
#   return username, password

#Prompt for username once and password twice, return both.
#While loop to ask for password twice to verify that it was typed correctly.
# def get_credentials():
#   username = get_input('   Enter Username: ')
#   password = None
#  	while not password:
#		password = getpass('   Enter Password: ')
#		password_verify = getpass('   Retype Password: ')
#		print()
#		if password != password_verify:
#			print('Passwords do not match. Please try again.')
#			password = None
#	return username, password
