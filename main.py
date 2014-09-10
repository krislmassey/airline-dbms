'''
Created on Sept 10, 2014

Project: DBMS Project
Name   : main.py

@authors: Kristen Massey and Nathan Smith
'''
'''
###############################################################################

Mississippi State University

Property of original authors Kristen Massey and Nathan Smith do not copy,
transfer, or disclose or you will be prosecuted blah blah blah...

###############################################################################

'''

import os
import sys
from AirbaseClass import Airbase


main():

    db = 'DatabaseName'     #Database Name
    host = '10.100.100.10'  #IP Address of machine
    username = 'root'       #Accessing User
    passwd = 'pass'         #User's password


    # could put all of the above in a .ini file for quick reference


    #Create db object
    MyDbObject = Airbase.Airbase(db, host, username, passwd)


    #Attempt connection demo

    print "Attempting Startup Demo..."
    try:
        MyDbObject.StartupDemo()
    except:
        print "Attempt failed."

    print "Attempt Success!"
    




    #end

    return None

    
