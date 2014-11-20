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



#################################################
###  DELETES ENTRY IN DATABASE (from existing table)
#################################################

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


#################################################
###  DISPLAYS ENTRIES IN DATABASE
#################################################
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
        try:
            self.select(table, columnstring, wherestring)
            self.printRows()
        except:
            print "Problem with query.  Try again."

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


######################################
###  DISPLAY CUSTOMER OPTIONS      ###
######################################

    def customerMode(self):
        print "Choose an option\n" + \
              "****************\n" + \
              "r          -make a reservation\n" + \
              "d          -delete a reservation\n" + \
              "f          -find flights for a round trip\n" + \
              "c          -calculate cost of flight(s)\n" + \
              "exit       -return to main option screen\n" + \
              "\n"
        choice = raw_input("Option:")

        if choice == 'r':
            self.reservation()
        elif choice == 'd':
            self.cancelReservation()
        elif choice == 'f':
            self.roundTrip()
        elif choice == 'c':
            self.costCalculator()
        elif choice == "exit":
            print ""
        else:
            print "Invalid input"
            self.customerMode()

        return None


######################################
###  MAKE A RESERVATION            ###
######################################
    def reserve(self, name, phone, flight_number, leg_numbers):
        for number in leg_numbers:
            self.select("Seats", "seat_number", "available=True AND flight_number="+flight_number)
            seat_number = self._cursor.fetchone()
            if not self.update("Seats", "name,phone_number,available", name+","+phone+",false", "seat_number="+seat_number):
                print "Error reserving seat "+seat_number+" on leg "+number+"."
                return False
            elif not self.update("Leg_Schedule", "available_seat_number", "available_seat_number - 1", "leg_number="+number):
                print "Error decrementing available seat number on leg "+number+"."
            else:
                "Seat "+seat_number+" reserved on leg "+number+".\n"


    def reservation(self):
        #edits info on Seats table and leg_schedule table (decrements available seats)

        #ask user for
        #Name
        name = raw_input("Enter your name: ")
        #phone number (XXX)-XXX-XXXX
        phone = raw_input("Enter your phone number in format (xxx)-xxx-xxx: ")
        #flight number
        flight_number = raw_input("Enter the flight number: ")
        #check if flight_number exists
        self.select("Flights", "flight_number", "flight_number = "+flight_number)
        if not self._cursor.fetchone():
            print "Flight number " + flight_number + " not found. Please select a valid flight.\n"
            return -1
        #leg number (make it where they can add multiple at a time
        leg_numbers = raw_input("Enter the leg number(s), separated by commas: ")
        #check if leg numbers exist
        leg_numbers = leg_numbers.split(",")
        for number in leg_numbers:
            self.select("Leg_Schedule", "leg_number", "leg_number = "+number.strip())
            if not self._cursor.fetchone():
                print "Leg number " + number + "not found. Please select a valid leg.\n"
                return -1
        #display the total cost and confirm
        confirm = raw_input("Are you sure you want to reserve this flight? (Y/N): ")
        if confirm.upper() == "N":
            return -1
        elif confirm.upper() == "Y":
            self.reserve(name, phone, flight_number, leg_numbers)
        else:
            return -1
        #autofill seat number
        #Decrement leg_schedule.seats_available for all legs selected
        return None


######################################
###  CANCEL A RESERVATION          ###
######################################
    def cancelReservation(self):

        #delete rows from Seats where flight=user_input_flight
        #and where leg_number = user_input_leg_number
        #and where passenter name = user_input_name

        #decrement legs for every leg entered
        return None

######################################
###  FIND A ROUND TRIP             ###
######################################
    def roundTrip(self):
        #get necessary user input
        start_City = raw_input("Enter the name of the departure city: ")
        start_State = raw_input("Enter the initials of the departure state: ")
        end_City = raw_input("Enter the name of the destination city: ")
        end_State = raw_input("Enter the initials of the destination state: ")
        departDate = raw_input("Enter the departure flight date (ex: 10/06/2014): ")
        returnDate = raw_input("Enter the return flight date (ex: 10/06/2014): ")

        #create variables to hold lists
        startFlight_list = []
        returnFlight_list = []


        #get list of all possible flights to the destination and list of all possible flight back
        startFlight_list = self.oneWayTrip(start_City, start_State, end_City, end_State, departDate)
        returnFlight_list = self.oneWayTrip(end_City, end_State, start_City, start_State, returnDate)


        #print possible start flights
        if len(startFlight_list) == 0:
            print "Outset Flight Options:  \nNone"
        else:
            print "Outset Flight Options: \n"
            for item in startFlight_list:
                print str(item) + "\n"

        #print possible return flights
        if len(returnFlight_list) == 0:
            print "Return Flight Options:  \nNone"
        else:
            print "Return Flight Options:  \n"
            for item in returnFlight_list:
                print str(item) + "\n"


        return None



######################################
###  FIND VIABLE ONE-WAY TRIPS     ###
######################################
    def oneWayTrip(self, start_City, start_State, end_City, end_State, date):
        flight_list = []
        possibleFlight_list = []
        startFlight_list = []
        endFlight_list = []

        #first find all flights associated with all flight legs that start
        #in the start city, start state, on the date, put in a list
        selectString = "SELECT L.flight_number FROM Leg_Schedule L " + \
                       "INNER JOIN Airport A " + \
                       "ON A.city = '" + str(start_City) + "' AND A.state = '" + str(start_State) + "' AND A.airport_code = L.start_airport_code AND L.date = '" + str(date) + "';"
        self._cursor.execute(selectString)
        start_Tuple = self._cursor.fetchall()

        if start_Tuple is not None:
            #map the tuple to a list
            for item in start_Tuple:
                startFlight_list.append(str(item[0]))



        #next find all the flights that end in the end city and the end State
        #on the date specified, put in a list
        selectString = "SELECT L.flight_number FROM Leg_Schedule L " + \
                       "INNER JOIN Airport A " + \
                       "ON A.city = '" + end_City + "' AND A.state = '" + end_State + "' AND A.airport_code = L.end_airport_code AND L.date = '" + date + "';"
        self._cursor.execute(selectString)
        end_Tuple = self._cursor.fetchall()
        #map the tuple to a list (list formatting will be weird)
        if end_Tuple is not None:
            #map the items in the tuple to a list
            for item in end_Tuple:
                endFlight_list.append(str(item[0]))



        #check to see if any of the flights that match these criteria overlap,
        #if they do, put them into a new list
        for flight in startFlight_list:
            if flight in endFlight_list:
                possibleFlight_list.append(flight)

        #run the list of possible matches through routeCheck to make sure
        #that the leg path connects them for the date specified
        for flight in possibleFlight_list:
            flightWorks = self.routeCheck(flight, start_City, start_State, end_City, end_State, date)
            if flightWorks:
                flight_list.append(flight)

        return flight_list



#############################################################################
###  CHECK TO MAKE SURE THE FLIGHT CONNECTS THE START/END DESTINATION     ###
#############################################################################
    def routeCheck(self, flight, start_City, start_State, end_City, end_State, date):

        #find the leg for the specified flight that starts in the start city and get the end city/state for that flight
        #if no flight leg starts in the start city/state specified, return False

        #get the end airport code for the flight patching the criteria
        selectString = "SELECT L.end_airport_code FROM Leg_Schedule L " + \
                       "INNER JOIN Airport A " + \
                       "ON L.start_airport_code=A.airport_code " + \
                       "AND L.date = '" + str(date) + "' " + \
                       "AND L.flight_number='" + str(flight) + "' " + \
                       "AND A.city='" + str(start_City) + "' " + \
                       "AND A.state='" + str(start_State) + "';"

        self._cursor.execute(selectString)
        result_Tuple = self._cursor.fetchone()
        #if no result, return False
        if result_Tuple is None:
            flightWorks = False
            return flightWorks

        end_airport = result_Tuple[0] #gets end_airport_code from tuple



        #get end city and end state for end airport found from flight_leg
        selectString = "SELECT A.city, A.state " + \
                       "FROM Airport A " + \
                       "WHERE A.airport_code='" + str(end_airport) + "';"

        self._cursor.execute(selectString)
        result_Tuple = self._cursor.fetchone()

        if result_Tuple is None:
            flightWorks = False
            return flightWorks

        city = str(result_Tuple[0])
        state = str(result_Tuple[1])


        #check if the city/state found match the target city/state
        if city == end_City and state == end_State:
            flightWorks = True
        else:
            #if no, call routeChecker again with the end city/state as the new start city/state
            start_City = city
            start_State = state
            flightWorks = self.routeCheck(flight, start_City, start_State, end_City, end_State, date)
            #this keeps going until it finds a match or traverses the full flight path


        return flightWorks




######################################
###  CALCULATE COST OF TRIP(S)     ###
######################################
    def costCalculator(self):
        #get flight to calculate cost for
        #get flight class for ticket
        #check to make sure class available for that flight
            #if available, add and ask if they want to enter a new flight
            #if not available, print error message and prompt to enter a different flight

        addflight = True
        flight_list = []
        fare_list = []
        fare_cost_list = []

        fare_exists = False
        fare_for_flight = False
        cont = 'Y'

        while addflight:
            flight = raw_input("Enter flight number: ")
            #check flights table to make sure flight exists
            selectStatement = "SELECT * FROM Flights F WHERE F.flight_number='" + str(flight) + "';"
            self._cursor.execute(selectStatement)
            flightFound = self._cursor.fetchall()


            if flightFound is None:
                print "Error: Flight code not found in Airbase.\n"
                cont = raw_input("Continue?(Y/N): ")
                if cont == 'N' or cont == 'n':
                    break
                continue

            fare = raw_input("Enter fare code: ")
            #check fare table to make sure fare exists
            selectStatement = "SELECT * FROM Flight_Fares F WHERE F.flight_number='" + str(flight) + "' AND F.fare_code='" + str(fare) + "';"
            self._cursor.execute(selectStatement)
            fare_exists = self._cursor.fetchall()

            if fare_exists is None:
                print "Fare selected not available for flight specified"
                cont = raw_input("Continue?(Y/N): ")
                if cont == 'N' or cont == 'n':
                    break
                continue

            flight_list.append(flight)
            fare_list.append(fare)

            continue_entry = raw_input("Do you want to add another flight?(Y/N): ")
            if continue_entry == 'Y' or continue_entry == 'y':
                addflight = True
            else:
                addflight = False

            continue


        for fare in fare_list:
            #find cost of fare
            selectStatement = "SELECT F.fare_cost FROM Fares F WHERE F.fare_code='" + str(fare) + "';"
            self._cursor.execute(selectStatement)
            cost = self._cursor.fetchone()
            #put fare cost in fare_cost_list
            fare_cost_list.append(str(cost[0]))


        totalCost = 0.00
        if len(flight_list) > 0:
            for item in fare_cost_list:
                totalCost+=float(item)

        index = len(flight_list)
        x = 0

        #print out a table with all the flight numbers, fare codes, fare costs,
        #and a final row with the total cost for the tickets

        print "=========================================\n"
        print "+ Flight      Fare             Cost +\n"
        print "=========================================\n"
        while x<index:
            print "| " + flight_list[x] + "\t\t" + fare_list[x] + "\t\t$" + fare_cost_list[x] + " |\n"
            x+=1
        print "|_______________________________________|\n"
        print "| Total Cost:        " + str(totalCost) + " |\n"
        print "========================================\n"

        return None
