USE employee_db;

--creating a table 

CREATE TABLE employee(
	id INT IDENTITY PRIMARY KEY,
	name varchar(50),
	age SMALLINT,
	location varchar(50)
	);

--altering table columns
ALTER TABLE employee
ADD DOB date;

--describe the details of the table
EXEC sp_help employee

-- inserting rows into table
INSERT INTO employee 
VALUES('Tom',2,'USA','2019-10-20'),
		('Jerry',1,'USA','2019-03-10'),
		('Eric',2,'CANADA','2019-08-15');

--display the rows of the table
SELECT * FROM employee

--update data in the table
UPDATE employee
SET name = 'Donald'
WHERE name = 'Tom';

-- delete record from the table
DELETE FROM employee
WHERE name = 'Donald'

--deleting the table
DROP TABLE employee
