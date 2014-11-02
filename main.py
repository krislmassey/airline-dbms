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
import warnings
import traceback
import AirbaseClass


def main():

    db = 'Airbase'     #Database Name
    host = 'localhost'  #IP Address of machine
    username = 'root'       #Accessing User
    passwd = 'furuba'         #User's password


    # could put all of the above in a .ini file for quick reference


    #Create db object
    MyDbObject = Airbase.Airbase(db, host, username, passwd)


    #Attempt connection demo
    connectionSuccess = 0

    print "Attempting Startup Demo..."
    
    try:
        MyDbObject.Airbase.StartupDemo()
        connectionSuccess = 1
        print "Attempt Success!"
        
    except Exception, msg:
        print "Attempt failed."
        print 'Exception: %s' % msg
        traceback.print_exc()
        return None



    #Attempt actual Startup

    if connectionSuccess:

        print "Attempting Startup..."

        try:
            MyDbObject.Airbase.Startup()
            print "Attempt Success!"

        except Exception, msg:
            print "Attempt failed."
            print 'Exception: %s' % msg
            traceback.print_exc()
            return None
            
    
        
        
    
    #Go to User Options
    while 1:

        MyDbObject.Airbase.GetOptionMain()


    #end



    return None

    
main()
