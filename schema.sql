CREATE TABLE Airport (
UNIQUE Airport_Code DECIMAL (6,0) NOT NULL,
Airport_Name VARCHAR(50),
City VARCHAR(25),
State CHAR(2),
PRIMARY KEY (Airport_Code)
);

CREATE TABLE Flights (
UNIQUE Flight_Number INTEGER NOT NULL AUTO_INCREMENT,
Airline VARCHAR(25),
Start_Airport_Code DECIMAL(6,0) NOT NULL,
End_Airport_Code DECIMAL (6,0) NOT NULL,
PRIMARY KEY (Flight_Number),
FOREIGN KEY (Start_Airport_Code) REFERENCES Airport(Airport_Code),
FOREIGN KEY (End_Airport_Code) REFERENCES Airport(Airport_Code)
);

CREATE TABLE Fares (
UNIQUE Fare_Code INTEGER NOT NULL AUTO_INCREMENT,
Flight_Number INTEGER NOT NULL,
Fare_Cost DECIMAL (5,2),
Fare_Restrictions VARCHAR(1000),
PRIMARY KEY (Fare_Code),
FOREIGN KEY (Flight_Number) REFERENCES Flights(Flight_Number)
);

CREATE TABLE Airplane (
UNIQUE Tail_Number INTEGER NOT NULL,
Seat_Number INTEGER,
Max_Seat_Number INTEGER,
Model VARCHAR(25),
Manufacturer VARCHAR(25),
CHECK (Seat_Number < Max_Seat_Number),
PRIMARY KEY (Tail_Number)
);

CREATE TABLE Leg_Schedule (
UNIQUE Leg_Number INTEGER NOT NULL AUTO_INCREMENT,
Flight_Number INTEGER NOT NULL,
Start_Airport_Code DECIMAL(6,0) NOT NULL,
End_Airport_Code DECIMAL (6,0) NOT NULL,
Scheduled_Departure_Time VARCHAR(20),
Scheduled_Arrival_Time VARCHAR(20),
Date VARCHAR(20),
Available_Seat_Number INTEGER,
PRIMARY KEY (Leg_Number),
FOREIGN KEY (Leg_Number) REFERENCES Leg_Instance(Leg_Number),  //This statement wont work until (Leg_Instance) is created and will have to be added in later in an “Alter Table” command //
FOREIGN KEY (Flight_Number) REFERENCES Flights(Flight_Number),
FOREIGN KEY (Start_Airport_Code) REFERENCES Airport(Airport_Code),
FOREIGN KEY (End_Airport_Code REFERENCES Airport(Airport_Code)
);

CREATE TABLE Leg_Instance (
UNIQUE Leg_Number INTEGER NOT NULL,
Flight_Number INTEGER NOT NULL,
Actual_Departure_Time VARCHAR(20),
Actual_Arrival_Time VARCHAR(20),
Tail_Number INTEGER NOT NULL,
Date VARCHAR(20)
PRIMARY KEY(Leg_Number),
FOREIGN KEY (Flight_Number) REFERENCES Flights(Flight_Number),
FOREIGN KEY (Tail_Number) REFERENCES Airplane(Tail_Number)
);

CREATE TABLE Seats (
Seat_Number VARCHAR(4) NOT NULL,
Passenger_Name VARCHAR(20),
Passenger_Phone INTEGER,
Flight_Number INTEGER NOT NULL,
Leg_Number DECIMAL(12,0) NOT NULL,
Available CHAR(1),
FOREIGN KEY (Flight_Number) REFERENCES Flights(Flight_Number),
FOREIGN KEY (Leg_Number) REFERENCES Leg_Instance(Leg_Number)
);

CREATE TABLE Flight_Days (
Flight_Number INTEGER NOT NULL,
Monday CHAR(1),
Tuesday CHAR(1),
Wednesday CHAR(1),
Thursday CHAR(1),
Friday CHAR(1),
Saturday CHAR(1),
Sunday CHAR(1),
FOREIGN KEY (Flight_Number) REFERENCES Flights(Flight_Number)
);

CREATE TABLE Landing_Allowances (
Model VARCHAR(20) NOT NULL,
Airport_Code DECIMAL(6,0) NOT NULL,
Allowed CHAR(3) NOT NULL
);