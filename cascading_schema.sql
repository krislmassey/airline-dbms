DROP TABLE IF EXISTS Landing_Allowances;
DROP TABLE IF EXISTS Flight_Days;
DROP TABLE IF EXISTS Seats;
DROP TABLE IF EXISTS Leg_Instance;
DROP TABLE IF EXISTS Leg_Schedule;
DROP TABLE IF EXISTS Airplane;
DROP TABLE IF EXISTS Airplane_Type;
DROP TABLE IF EXISTS Flight_Fares;
DROP TABLE IF EXISTS Flights;
DROP TABLE IF EXISTS Fares;
DROP TABLE IF EXISTS Airport;

CREATE TABLE Airport (
airport_code VARCHAR(6) UNIQUE NOT NULL,
airport_name VARCHAR(50),
city VARCHAR(25),
state VARCHAR(2),
PRIMARY KEY (airport_code)
);

CREATE TABLE Fares (
fare_code INTEGER UNIQUE NOT NULL AUTO_INCREMENT,
fare_cost DECIMAL (5,2),
fare_restrictions VARCHAR(1000),
PRIMARY KEY (fare_code)
);

CREATE TABLE Flights (
flight_number INTEGER UNIQUE NOT NULL AUTO_INCREMENT,
airline VARCHAR(25),
start_airport_code VARCHAR(6) NOT NULL,
end_airport_code VARCHAR(6) NOT NULL,
PRIMARY KEY (flight_number),
FOREIGN KEY (start_airport_code) REFERENCES Airport(airport_code) ON UPDATE CASCADE,
FOREIGN KEY (end_airport_code) REFERENCES Airport(airport_code) ON UPDATE CASCADE,
FOREIGN KEY (fare_code) REFERENCES Fares(fare_code)ON UPDATE CASCADE
);

CREATE TABLE Flight_Fares (
fare_code INTEGER NOT NULL,
flight_number INTEGER NOT NULL,
FOREIGN KEY (fare_code) REFERENCES Fares(fare_code) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (flight_number) REFERENCES Flights(flight_number) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Airplane_Type (
model VARCHAR(25) UNIQUE NOT NULL,
manufacturer VARCHAR(25),
max_seat_number INTEGER,
PRIMARY KEY (model)
);

CREATE TABLE Airplane (
tail_number INTEGER UNIQUE NOT NULL,
seat_number INTEGER,
model VARCHAR(25) NOT NULL,
PRIMARY KEY (tail_number),
FOREIGN KEY (model) REFERENCES Airplane_Type(model) ON UPDATE CASCADE
);

CREATE TABLE Leg_Schedule (
leg_number INTEGER UNIQUE NOT NULL AUTO_INCREMENT,
flight_number INTEGER NOT NULL,
start_airport_code VARCHAR(6) NOT NULL,
end_airport_code VARCHAR(6) NOT NULL,
scheduled_departure_time VARCHAR(20),
scheduled_arrival_time VARCHAR(20),
date VARCHAR(20),
available_seat_number INTEGER,
PRIMARY KEY (leg_number),
FOREIGN KEY (flight_number) REFERENCES Flights(flight_number) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (start_airport_code) REFERENCES Airport(airport_code) ON UPDATE CASCADE,
FOREIGN KEY (end_airport_code) REFERENCES Airport(airport_code) ON UPDATE CASCADE
);

CREATE TABLE Leg_Instance (
leg_number INTEGER UNIQUE NOT NULL,
flight_number INTEGER NOT NULL,
actual_departure_time VARCHAR(20),
actual_arrival_time VARCHAR(20),
tail_number INTEGER NOT NULL,
date VARCHAR(20),
PRIMARY KEY(leg_number),
FOREIGN KEY (flight_number) REFERENCES Flights(flight_number) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (tail_number) REFERENCES Airplane(tail_number) ON UPDATE CASCADE,
FOREIGN KEY (leg_number) REFERENCES Leg_Schedule(leg_number) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Seats (
seat_number VARCHAR(4) NOT NULL,
passenger_name VARCHAR(20),
passenger_phone INTEGER,
flight_number INTEGER NOT NULL,
leg_number INTEGER NOT NULL,
available BOOLEAN,
FOREIGN KEY (flight_number) REFERENCES Flights(flight_number) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (leg_number) REFERENCES Leg_Instance(leg_number) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Flight_Days (
flight_number INTEGER NOT NULL,
monday CHAR(1),
tuesday CHAR(1),
wednesday CHAR(1),
thursday CHAR(1),
friday CHAR(1),
saturday CHAR(1),
sunday CHAR(1),
FOREIGN KEY (flight_number) REFERENCES Flights(flight_number) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Landing_Allowances (
model VARCHAR(20) NOT NULL,
airport_code VARCHAR(6) NOT NULL,
allowed BOOLEAN NOT NULL,
FOREIGN KEY (model) REFERENCES Airplane_Type(model) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (airport_code) REFERENCES Airport(airport_code) ON UPDATE CASCADE ON DELETE CASCADE
);