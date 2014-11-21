
INSERT INTO Airport
VALUES ('100000','Hartsfield-Jackson','Atlanta','GA');

INSERT INTO Airport
VALUES ('200000','Medgar Evers','Jackson','MS');

INSERT INTO Airport
VALUES ('300000','Huntsville International','Huntsville','AL');


INSERT INTO Airport
VALUES ('400000','George Bush Intercontinental','Houston','TX');


INSERT INTO Airport
VALUES ('500000','Nashville International','Nashville International','TN');


INSERT INTO Airport
VALUES ('600000','Sky Harbor','Phoenix','AZ');

INSERT INTO Airport
VALUES ('700000','Salt Lake International','Salt Lake City','UT');

INSERT INTO Airport
VALUES ('800000','Golden Triangle Regional','Starkville','MS');

INSERT INTO Airport
VALUES ('900000','Orlando International','Orlando','FL');



INSERT INTO Flights
VALUES ('1','American','600000','900000');

INSERT INTO Flights
VALUES('2','Southwest','100000','700000');

INSERT INTO Flights
VALUES('3','Jetblue','800000','800000');

INSERT INTO Flights
VALUES('4','Frontier','400000','200000');

INSERT INTO Flights
VALUES('5','US Airways','300000','500000');


INSERT INTO Fares
VALUES('1','260.00','First class');

INSERT INTO Fares
VALUES('2','200.00','Second class');

INSERT INTO Fares
VALUES('3','150.00','Economy');

INSERT INTO Fares
VALUES('4','600.00','Private cabin');

INSERT INTO Fares
VALUES('5','0.00','Airport personnel only');



INSERT INTO Leg_Schedule
VALUES('1','1','600000','300000','0','0','1/12/2014','5');

INSERT INTO Leg_Schedule
VALUES('2','1','300000','500000','0','0','1/12/2014','5');

INSERT INTO Leg_Schedule
VALUES('3','1','500000','900000','0','0','1/12/2014','5');

INSERT INTO Leg_Schedule
VALUES('4','2','100000','200000','0','0','1/14/2014','5');

INSERT INTO Leg_Schedule
VALUES('5','2','200000','800000','0','0','1/14/2014','5');

INSERT INTO Leg_Schedule
VALUES('6','2','800000','300000','0','0','1/14/2014','5');

INSERT INTO Leg_Schedule
VALUES('7','2','300000','700000','0','0','1/14/2014','5');

INSERT INTO Leg_Schedule
VALUES('8','3','800000','400000','0','0','1/12/2014','5');

INSERT INTO Leg_Schedule
VALUES('9','3','400000','800000','0','0','1/12/2014','5');

INSERT INTO Leg_Schedule
VALUES('10','4','400000','800000','0','0','1/14/2014','5');

INSERT INTO Leg_Schedule
VALUES('11','4','800000','100000','0','0','1/14/2014','5');

INSERT INTO Leg_Schedule
VALUES('12','4','100000','200000','0','0','1/14/2014','5');

INSERT INTO Leg_Schedule
VALUES('13','5','300000','200000','0','0','1/12/2014','5');

INSERT INTO Leg_Schedule
VALUES('14','5','200000','400000','0','0','1/12/2014','5');

INSERT INTO Leg_Schedule
VALUES('15','5','400000','800000','0','0','1/12/2014','5');

INSERT INTO Leg_Schedule
VALUES('16','5','800000','500000','0','0','1/12/2014','5');



INSERT INTO Flight_Fares
VALUES('1','1');

INSERT INTO Flight_Fares
VALUES('2','1');

INSERT INTO Flight_Fares
VALUES('3','1');

INSERT INTO Flight_Fares
VALUES('5','1');

INSERT INTO Flight_Fares
VALUES('1','2');

INSERT INTO Flight_Fares
VALUES('3','2');

INSERT INTO Flight_Fares
VALUES('5','2');

INSERT INTO Flight_Fares
VALUES('2','3');

INSERT INTO Flight_Fares
VALUES('3','3');

INSERT INTO Flight_Fares
VALUES('5','3');

INSERT INTO Flight_Fares
VALUES('1','4');

INSERT INTO Flight_Fares
VALUES('4','4');

INSERT INTO Flight_Fares
VALUES('5','4');

INSERT INTO Flight_Fares
VALUES('1','5');

INSERT INTO Flight_Fares
VALUES('2','5');

INSERT INTO Flight_Fares
VALUES('4','5');

INSERT INTO Flight_Fares
VALUES('5','5');



INSERT INTO Seats
VALUES('1','1','1','1','1','1');

INSERT INTO Seats
VALUES('2','1','1','1','1','1');

INSERT INTO Seats
VALUES('3','1','1','1','1','1');

INSERT INTO Seats
VALUES('4','1','1','1','1','1');

INSERT INTO Seats
VALUES('5','1','1','1','1','1');


