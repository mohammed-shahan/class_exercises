CREATE DATABASE Railway

USE Railway

CREATE TABLE stops(
	id INT PRIMARY KEY NOT NULL,
	stop CHAR(3) NOT NULL
)

CREATE TABLE trains(
	id INT IDENTITY PRIMARY KEY NOT NULL,
	code CHAR(7) NOT NULL,
	dest INT NOT NULL FOREIGN KEY REFERENCES stops(id),
	berth INT NOT NULL,
	waitlist INT NOT NULL
)

CREATE TABLE passengers(
	id INT IDENTITY PRIMARY KEY NOT NULL,
	name VARCHAR(20) NOT NULL,
	age INT NOT NULL,
	dest INT NOT NULL FOREIGN KEY REFERENCES stops(id),
	train INT NOT NULL FOREIGN KEY REFERENCES trains(id),
	waitlist BIT DEFAULT(0)
)

INSERT INTO stops VALUES
(1, 'ALP'),
(2, 'ERN'),
(3, 'KZK')


INSERT INTO trains VALUES
('TVM_ALP', 1, 5, 2),
('TVM_ERN', 2, 5, 2),
('TVM_KZK', 3, 5, 2)


CREATE PROCEDURE getTrSeats
AS
BEGIN
	SELECT DISTINCT trains.code, trains.berth AS max_berth, booked AS booked_berth, trains.berth - tr.booked AS available_berth FROM trains
	LEFT JOIN 
		(SELECT trains.code, COUNT(*) AS booked FROM passengers
		LEFT JOIN trains ON trains.id = passengers.train
		WHERE passengers.waitlist = 0
		GROUP BY code) AS tr ON tr.code = trains.code
END

exec getTrSeats
CREATE PROCEDURE getTrWL
AS
BEGIN
	SELECT DISTINCT trains.code, trains.dest, trains.waitlist max_waitlist, tr.waitlist AS booked_waitlist, trains.waitlist - tr.waitlist AS available_waitlist FROM trains
	LEFT JOIN 
		(SELECT trains.code, COUNT(*) AS waitlist FROM passengers
		JOIN trains ON trains.id = passengers.train
		WHERE passengers.waitlist = 1
		GROUP BY code) AS tr ON tr.code = trains.code
END
exec getTrWL

SELECT * FROM trains
SELECT * FROM stops
SELECT * FROM passengers