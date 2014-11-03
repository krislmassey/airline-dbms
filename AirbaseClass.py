'''
Created on Sept 10, 2014

Project: DBMS Project
Name   : Airbase.py

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
import MySQLdb
import re
import warnings


class Airbase(object):

'''
Functions in Class
'''

#################################################
###  iNITIALIZE CLASS OBJECT
#################################################

    def __init__(self, db='', host='', user='', passwd=''):
        self.db = db
        self.host = host
        self.user = user
        self.passwd = passwd

        #getting username, host ip, database name, and password for connection


        return None
        #end __init__

#################################################
###  DEMO PYTHON STARTUP DATABASE CONNECTION
#################################################

    def startupDemo(self):

        #get database connection
        self._DBconnection = MySQLdb.connect(self._host, self._user, self._passwd, self._db)
        print "Database connection successful"

        #create cursor
        self._cursor = self._DBconnection.cursor()
        print "Cursor creation successful"


        #close connection
        self._DBconnection.close()
        print "Database connection closed"


        return None
        #end StartupDemo


#################################################
###  PYTHON STARTUP DATABASE CONNECTION
#################################################    

    def startup(self):

        #get database connection
        self._DBconnection = MySQLdb.connect(self._host, self._user, self._passwd, self._db)
        print "Database connection successful"

        #create cursor
        self._cursor = self._DBconnection.cursor()
        print "Cursor creation successful"

        return None
        #end Startup


#################################################
###  CLOSE DATABASE CONNECTION
#################################################

    def closeDB(self):
        try:
            self._DBconnection.close()
            print "Airbase Connection Closed"
        except:
            "Error closing Airbase Connection."
            pass
        
        return None
        #end CloseDB


#################################################
###  GET USER OPTIONS FOR DATABASE VIEWING/EDITTING
################################################# 

    def getOptionMain(self):

        print "Enter option, for list of options enter 'help'"

        option = raw_input()

        #print instructions for User Input
        if option == 'help':
            print "Valid Airbase Commands Listed Below:" + \
                  "====================================" + \
                  "" + \
                  "e     -make a new entry\n" + \
                  "u     -update an existing entry\n" + \
                  "d     -delete an existing entry\n" + \
                  "v     -view all entries in a table\n" + \
                  "f     -find an entry in a table\n" + \
                  "exit  -close Airbase\n" + \
                  "\n"

        elif option == 'e':
            self.newEntry()
        elif option == 'u':
            self.updateEntry()
        elif option == 'd':
            self.deleteEntry()
        elif option == 'v':
            self.createView()
        elif option == 'f':
            self.findEntry()
        elif option == 'exit':
            self.closeDB()
        else:
            print "Invalid input.\n"
            

        return None
        #end GetOptionMain


#################################################
###  DELETE STATEMENT FUNCTION
#################################################

    def delete(self, table, columnstring, valuestring):

        op_status = 0

        

        return op_status  #0 on failure, 1 on success

#################################################
###  INSERT STATEMENT FUNCTION
#################################################

    def insert(self, table, columnstring, valuesstring):

        op_status = 0

        table = raw_input("Enter the name of the table to alter:")
        
        #warning, the lines below are case sensitive and cannot have spaces
        columnstring = raw_input("Enter the name of the columns to alter (separated by commas):")
        valuesstring = raw_input("Enter the values to enter into the columns (separated by commas):")

        #have to edit/parse the values entered in columnstring and valuesstring
        #at this point so they will fit with the SQL statement below (individual
        #items need to be separated by apostrophes)

        columns_L = columnstring.split(',')  #parse the strings into lists
        values_L = valuesstring.split(',')

        valuesstring = '\',\''.join(values_L)
        columnstring = '\',\''.join(columns_L)  #joins the lists back into appropriately formatted strings

        SQLstatement = "INSERT INTO '" + table + "('" + columnstring + "')" + \
                       "' VALUES('" + valuesstring + "');"

        self.dbWrite(SQLstatement);


        return op_status #0 on failure, 1 on success



#################################################
###  UPDATE STATEMENT FUNCTION
#################################################
    def update(self, table, columnstring, valuesstring):

        op_status = 0

        return op_status #0 on failure, 1 on success



#################################################
###  SELECT STATEMENT FUCTION
#################################################
    def select(self, table, columnstring, wherestring):
        query = "SELECT {columns} FROM {table} WHERE {wherestring}".format(columnstring, table, wherestring)
        return self.dbWrite(query)

    def newEntry(self):
        return None

    def updateEntry(self):
        return None

    def deleteEntry(self):
        return None

    def createView(self):
        return None

    def findEntry(self):
        return None



#################################################
###  SQL STATEMENT WRITE FUNCTION 
#################################################
    def dbWrite(self, SQLstatement):
        op_status = 0
        
        try:
            self._cursor.execute(SQLstatement)
            op_status = 1
            
        except Exception, msg:
            #elevates sql write error to user
            warnings.warn(msg, Warning)
            
        return op_status #0 on failure, 1 on success


        
