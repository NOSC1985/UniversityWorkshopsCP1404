"""
Program: woefully_inadequate_security
Author: Nicholas Stanton-Cook
Program Set: Week five Workshop Tasks
This program will ask the user for an input of of a user name string and then
check the user data agains a set of approved user names in a data base list.
it prints Access Granted if the input user name matches any of the names in the Data Base list.
"""
__Author__= "Nicholas Stanton-Cook"

"""
Generate the Constant User_Names Data Base
(Note: could be imported from file, for more flexibility and to be more reusable)

user_name = get user input

if user_name == any strings in User_Names
    Acess granted

else
    Access Denied

"""

USER_NAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


input_user_name = input(":")
if ("{}".format(input_user_name) in USER_NAMES) is True:
    print("Access Granted")
else:
    print("Access Denied\nPlease Try Again")
