'''
Created on Sept 10, 2014

Project: DBMS Project
Name   : Airbase.py

@authors: Kristen Massey and Nathan Smith

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
        self._DBconnection = MySQLdb.connect(self.host, self.user, self.passwd, self.db)
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
        self._DBconnection = MySQLdb.connect(self.host, self.user, self.passwd, self.db)
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
            print "Valid Airbase Commands Listed Below:\n" + \
                  "====================================\n" + \
                  "\n" + \
                  "e     -make a new entry\n" + \
                  "u     -update an existing entry\n" + \
                  "d     -delete an existing entry\n" + \
                  "v     -view all entries in a table\n" + \
                  "f     -find an entry in a table\n" + \
                  "c     -customer operations\n" + \
                  "exit  -close Airbase\n" + \
                  "\n"

        elif option.lower() == 'e':
            self.newEntry()
        elif option.lower() == 'u':
            self.updateEntry()
        elif option.lower() == 'd':
            self.deleteEntry()
        elif option.lower() == 'v':
            self.displayTable()
        elif option.lower() == 'f':
            self.findEntry()
        elif option.lower() == 'c':
            self.customerMode()
        elif option.lower() == 'exit':
            self.closeDB()
            sys.exit()
        else:
            print "Invalid input.\n"


        return None
        #end GetOptionMain


#################################################
###  DELETE STATEMENT FUNCTION
#################################################

    def delete(self, table, wherestring=None):
        query = "DELETE FROM "+table
        if wherestring:
            query += " WHERE "+wherestring
        return self.dbWrite(query)

#################################################
###  INSERT STATEMENT FUNCTION
#################################################

    def insert(self, table, columnstring, valuesstring):

        op_status = 0

        #have to edit/parse the values entered in columnstring and valuesstring
        #at this point so they will fit with the SQL statement below (individual
        #items need to be separated by apostrophes)

        values_L = valuesstring.split(',')
        valuesstring = '\',\''.join(values_L)

        SQLstatement = "INSERT INTO "+table+"("+columnstring+") VALUES('"+valuesstring+"')"
        print SQLstatement
        op_status = self.dbWrite(SQLstatement);


        return op_status #0 on failure, 1 on success



#################################################
###  UPDATE STATEMENT FUNCTION
#################################################
    def update(self, table, columnstring, valuesstring, wherestring=None):

        op_status = 0

        #have to edit/parse the values entered in columnstring and valuesstring
        #at this point so they will fit with the SQL statement below (individual
        #items need to be separated by apostrophes)

        values_L = valuesstring.split(',')
        columns_L = columnstring.split(',')

        setstring = ""
        first = True
        for col, val in zip(columns_L, values_L):
            if first:
                setstring += col+"='"+val+"'"
                first = False
            else:
                setstring += ", "+col+"='"+val+"'"

        SQLstatement = "UPDATE "+table+" SET "+setstring
        if wherestring:
            SQLstatement += " WHERE "+wherestring

        op_status = self.dbWrite(SQLstatement);

        return op_status #0 on failure, 1 on success



#################################################
###  SELECT STATEMENT FUCTION
#################################################
    def select(self, table, columnstring, wherestring = None):
        query = "SELECT "+columnstring+" FROM "+table
        #Add the wherestring if there is one
        if wherestring:
            query += " WHERE "+wherestring
        return self.dbWrite(query)


#################################################
###   ENTRY IN DATABASE (to existing table)
#################################################

    def newEntry(self):

        #success variable (1 if true, 0 if false) determines if operation ran successfully

        #get input from the user
        table = raw_input("Enter the name of the table to alter:")

        #warning, the lines below are case sensitive and cannot have spaces
        columnstring = raw_input("Enter the name of the columns to alter (separated by commas):")
        valuesstring = raw_input("Enter the values to enter into the columns (separated by commas):")

        #do a check here to make sure an entry by that primary key doesn't already exist, need a function
        #for this called checkEntry.  Function will return 1 if the entry already exists, 0 if it doesnt.

        entryExists = 0

        if entryExists:
            print "An entry for the value specified already exists.  Do you want to overwrite it?"
            updateEntry = raw_input("Overwrite?(Y/N):")
            if updateEntry == 'Y':
                success = self.update(table, columnstring, valuesstring)
            else:
                print "Operation Cancelled"

        else:
            success = self.insert(table, columnstring, valuesstring)

        if success:
            self._DBconnection.commit()
            print "Change(s) submitted successfully."

        return None
        #end of newEntry


#################################################
###  NEW ENTRY IN DATABASE (to existing table)
#################################################
    def updateEntry(self):
        #success variable (1 if true, 0 if false) determines if operation ran successfully

        #get input from the user
        table = raw_input("Enter the name of the table to alter: ")

        #warning, the lines below are case sensitive and cannot have spaces
        columnstring = raw_input("Enter the name of the columns to alter (separated by commas): ")
        valuesstring = raw_input("Enter the values to enter into the columns (separated by commas): ")
        wherestring = raw_input("Enter the condition to check: ")
        if wherestring == '':
            wherestring = None

        #do a check here to make sure an entry by that primary key doesn't already exist, need a function
        #for this called checkEntry.  Function will return 1 if the entry already exists, 0 if it doesnt.

        entryExists = 0

        if entryExists:
            print "An entry for the value specified already exists.  Do you want to overwrite it?"
            updateEntry = raw_input("Overwrite?(Y/N):")
            if updateEntry == 'Y':
                success = self.update(table, columnstring, valuesstring)
            else:
                print "Operation Cancelled"

        else:
            success = self.update(table, columnstring, valuesstring, wherestring)

        if success:
            self._DBconnection.commit()
            print "Change(s) submitted successfully."

        return None

    def deleteEntry(self):
        #success variable (1 if true, 0 if false) determines if operation ran successfully

        #get input from the user
        table = raw_input("Enter the name of the table to alter: ")

        #warning, the lines below are case sensitive and cannot have spaces
        wherestring = raw_input("Enter the condition to check: ")
        if wherestring == '':
            wherestring = None

        #do a check here to make sure an entry by that primary key doesn't already exist, need a function
        #for this called checkEntry.  Function will return 1 if the entry already exists, 0 if it doesnt.

        entryExists = 0

        if entryExists:
            print "An entry for the value specified already exists.  Do you want to overwrite it?"
            updateEntry = raw_input("Overwrite?(Y/N):")
            if updateEntry == 'Y':
                success = self.update(table, columnstring, valuesstring)
            else:
                print "Operation Cancelled"

        else:
            success = self.delete(table, wherestring)

        if success:
            self._DBconnection.commit()
            print "Change(s) submitted successfully."

        return None

    def displayTable(self):
        """Prints all columns in a single table"""
        table = raw_input("Enter table to display: ")

        if self.select(table, '*'):
            self.printRows()

        return None


#################################################
###  FIND ENTRY IN DATABASE (in existing table)
#################################################
    def findEntry(self):
        table = raw_input("Enter the name of the table to query: ")

        #warning, the lines below are case sensitive and cannot have spaces
        columnstring = raw_input("Enter the names of the columns to query (separated by commas): ")
        wherestring = raw_input("Enter the wherestring: ")
        if wherestring == '':
            wherestring = None

        if self.select(table, columnstring, wherestring):
            self.printRows()

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

######################################
###  DISPLAY SQL RESULTS FUNCTION  ###
######################################

    def printRows(self):
        #http://stackoverflow.com/questions/10865483/print-results-in-mysql-format-with-python
        results = self._cursor.fetchall()
        widths = []
        columns = []
        tavnit = '|'
        separator = '+'

        for cd in self._cursor.description:
            widths.append(max(cd[2], len(cd[0])))
            columns.append(cd[0])

        for w in widths:
            tavnit += " %-"+"%ss |" % (w,)
            separator += '-'*w + '--+'

        print(separator)
        print(tavnit % tuple(columns))
        print(separator)
        for row in results:
            print(tavnit % row)
        print(separator)
