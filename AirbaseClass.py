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

    def StartupDemo(self):

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

    def Startup(self):

        #get database connection
        self._DBconnection = MySQLdb.connect(self._host, self._user, self._passwd, self._db)
        print "Database connection successful"

        #create cursor
        self._cursor = self._DBconnection.cursor()
        print "Cursor creation successful"

        return None
        #end Startup



    def GetOptionMain(self):

        print "Enter option, for list of options enter 'help'"

        option = raw_input()

        #print instructions for User Input

        return None
        #end GetOptionMain

    def select(self, values, table, condition):
        """Generic select, returns all rows"""
        query = "SELECT %s FROM %s WHERE %s"
        self.cursor.execute(query, (values, table, condition))
        rows = self.cursor.fetchall()
        return rows

    def select_one(self, values, table, condition):
        """Generic select function, returns first row"""
        query = "SELECT %s FROM %s WHERE %s"
        self.cursor.execute(query, (values, table, condition))
        row = self.cursor.fetchone()
        return row

    def insert(self, table, columns, values):
        """Generic insert function, returns false on failure"""
        if len(columns) != len(values):
            return False

        all_values = [table] + [col for col in columns] + [val for val in values]
        all_values = tuple(all_values)
        query = "INSERT INTO %s("

        #Add column fields
        first = True
        for i in range(len(columns)):
            if first:
                query += "%s"
                first = False
            else:
                query += ", %s"

        query += ") VALUES("

        #Add value fields
        first = True
        for i in range(len(values):
            if first:
                query += "%s"
                first = False
            else:
                query += ", %s"

        query += ")"
        #execute the query
        self.cursor.execute(query, all_values)
