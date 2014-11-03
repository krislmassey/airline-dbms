DROP TABLE IF EXISTS Landing_Allowances;
DROP TABLE IF EXISTS Flight_Days;
DROP TABLE IF EXISTS Seats;
DROP TABLE IF EXISTS Leg_Instance;
DROP TABLE IF EXISTS Leg_Schedule;
DROP TABLE IF EXISTS Airplane;
DROP TABLE IF EXISTS Fares;
DROP TABLE IF EXISTS Flights;
DROP TABLE IF EXISTS Airport;

CREATE TABLE Airport (
Airport_Code DECIMAL (6,0) UNIQUE NOT NULL,
Airport_Name VARCHAR(50),
City VARCHAR(25),
State CHAR(2),
PRIMARY KEY (Airport_Code)
);

CREATE TABLE Flights (
Flight_Number INTEGER UNIQUE NOT NULL AUTO_INCREMENT,
Airline VARCHAR(25),
Start_Airport_Code DECIMAL(6,0) NOT NULL,
End_Airport_Code DECIMAL (6,0) NOT NULL,
PRIMARY KEY (Flight_Number),
FOREIGN KEY (Start_Airport_Code) REFERENCES Airport(Airport_Code),
FOREIGN KEY (End_Airport_Code) REFERENCES Airport(Airport_Code)
);

CREATE TABLE Fares (
Fare_Code INTEGER UNIQUE NOT NULL AUTO_INCREMENT,
Flight_Number INTEGER NOT NULL,
Fare_Cost DECIMAL (5,2),
Fare_Restrictions VARCHAR(1000),
PRIMARY KEY (Fare_Code),
FOREIGN KEY (Flight_Number) REFERENCES Flights(Flight_Number)
);

CREATE TABLE Airplane (
Tail_Number INTEGER UNIQUE NOT NULL,
Seat_Number INTEGER,
Max_Seat_Number INTEGER,
Model VARCHAR(25),
Manufacturer VARCHAR(25),
CHECK (Seat_Number < Max_Seat_Number),
PRIMARY KEY (Tail_Number)
);

CREATE TABLE Leg_Schedule (
Leg_Number INTEGER UNIQUE NOT NULL AUTO_INCREMENT,
Flight_Number INTEGER NOT NULL,
Start_Airport_Code DECIMAL(6,0) NOT NULL,
End_Airport_Code DECIMAL (6,0) NOT NULL,
Scheduled_Departure_Time VARCHAR(20),
Scheduled_Arrival_Time VARCHAR(20),
Leg_Date VARCHAR(20),
Available_Seat_Number INTEGER,
PRIMARY KEY (Leg_Number),
FOREIGN KEY (Flight_Number) REFERENCES Flights(Flight_Number),
FOREIGN KEY (Start_Airport_Code) REFERENCES Airport(Airport_Code),
FOREIGN KEY (End_Airport_Code) REFERENCES Airport(Airport_Code)
);

CREATE TABLE Leg_Instance (
Leg_Number INTEGER UNIQUE NOT NULL,
Flight_Number INTEGER NOT NULL,
Actual_Departure_Time VARCHAR(20),
Actual_Arrival_Time VARCHAR(20),
Tail_Number INTEGER NOT NULL,
Leg_Date VARCHAR(20),
PRIMARY KEY(Leg_Number),
FOREIGN KEY (Flight_Number) REFERENCES Flights(Flight_Number),
FOREIGN KEY (Tail_Number) REFERENCES Airplane(Tail_Number)
);

CREATE TABLE Seats (
Seat_Number VARCHAR(4) NOT NULL,
Passenger_Name VARCHAR(20),
Passenger_Phone INTEGER,
Flight_Number INTEGER NOT NULL,
Leg_Number INTEGER NOT NULL,
Available BOOLEAN,
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