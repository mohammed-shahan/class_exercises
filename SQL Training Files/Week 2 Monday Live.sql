USE employee_db


--Popular string functions
--------------------------

--to get the ASCII value for the char
SELECT ASCII('B')

--Search sub string inside a string
SELECT CHARINDEX('World','Hello World') --position of first occurence will be returned

--to join together two strings
SELECT CONCAT('Hello','World')

--to check how the two string sound
SELECT SOUNDEX('Test'), SOUNDEX('Testing')

SELECT SOUNDEX('Tom'), SOUNDEX('Toum')

SELECT DIFFERENCE('Tom','Tomy')


--Tuesday


--select specific number of chars from left/right
SELECT LEFT('Hello World',5);
SELECT RIGHT('Hello World',5);

--converting string to lower case and upper case
SELECT LOWER ('Hello');
SELECT UPPER('HeLlo');

--trim unwanted space from left/right or both
SELECT TRIM('  HELLO')
SELECT LTRIM('  HELLO')
SELECT RTRIM('  HELLO')

--duplicate the string specificed number of times
SELECT REPLICATE ('Hello',5)


--popular date and time functions

--return current time stamp
SELECT CURRENT_TIMESTAMP AS DATE;

--return current date time
SELECT GETDATE() AS Date;

--get the UTC time
SELECT GETUTCDATE() AS Date

--get the precise time
SELECT SYSDATETIME() AS date;

--Extracting the part of date
--extract day
SELECT DATENAME(day,'2022/07/12')
--Extract month
SELECT DATENAME(month,'2022/07/12')
--extract year
SELECT DATENAME(year,'2022/07/12')

--extracting part of the day as integer

SELECT DATEPART(day,'2022/07/12')
SELECT DATEPART(month,'2022/07/12')
SELECT DATEPART(year,'2022/07/12')

-- FIND DATE, MONTH AND YEAR DIFFERENCE
SELECT DATEDIFF(DD,'2022/07/12','2022/08/10')

SELECT DATEDIFF(MM,'2022/07/30','2022/08/1')

-- DIFFERENCE IN WEEK
SELECT DATEDIFF(WK,'2022/07/12','2022/08/10')


--SQL Mathematical Functions
--To find square root
SELECT SQRT(49) as squareroot
--Find absolute value (without sign)
Select ABS(-34) as absolutevalue
--Round to the next highest value
SELECT CEILING(23.3) as roundhigh
--Round to the next lowest value
SELECT FLOOR(23.3) as roundlow
--find the power (exponential)
SELECT POWER(3,2) as threesquare
--find natural log
SELECT LOG(23) as log23
--to find the sign
SELECT SIGN(-10) as numbersign

--to generate pseudo random number
SELECT RAND()

--to generate a pseudo random number with seed
SELECT RAND(1501)

--sample Convert functions
--syntax is CONVERT(destination_data_type, expression_2_convert, length)
SELECT CONVERT(int, 45.23)  --converting a float to int
SELECT CONVERT(datetime,'2022-07-12')--converting a string to datetime
SELECT CONVERT(varchar, '2022-07-12',101)--converting string to varchar of length 100


--cast function (similar to CONVERT, but available in other DBMS too)
--syntax is CAST(expression_2_cast AS destination_data_type(length))
SELECT CAST(20.35 AS VARCHAR) --convert float into varchar of length 50
SELECT CAST('2022-07-12' AS datetime) --convert expression to datetime


-----JOIN------
--create table trainee
CREATE TABLE trainees(
     id int PRIMARY KEY Identity
    ,admin_no varchar (15) NOT NULL
    ,firstName varchar (45) NOT NULL
    ,lastName varchar (45) NOT NULL
    ,age int
    ,city varchar (25) NOT NULL
)

--create table fee
CREATE TABLE fee (
     admin_no varchar (45) NOT null
    ,semNo int NOT NULL
    ,course varchar (45) NOT NULL
    ,amount int
)

--create table semester
CREATE TABLE semester(
     semNo int NOT NULL
    ,semName varchar (10)
)

--adding some dummy data to trainee table
INSERT INTO trainees(admin_no,firstname,lastname,age,city) VALUES
(3354,'Spider','Man',13,'Texas'),
(2135,'James','Bond',13,'Alaska'),
(4321,'Jack','Sparrow',13,'California'),
(4213,'John','McClane',13,'New York'),
(5112,'Optimus','Prime',13,'Florida'),
(6113,'Captain','Kirk',13,'Arizona'),
(7555,'Harry','Potter',13,'New York'),
(8345,'Rose','Dawson',13,'California')


INSERT INTO semester (semno, semname) VALUES
(1,'First Sem'),
(2,'Second Sem'),
(3,'Third Sem'),
(4,'Fourth Sem')


INSERT INTO fee(admin_no,semNo,course,amount) VALUES
(3354,1,'Java',20000),
(7555,1,'Android',22000),
(4321,2,'Python',18000),
(8345,2,'SQL',15000),
(9345,2,'BlockChain',16000),
(9321,3,'Ethical Hacking',17000),
(5112,1,'Machine Learning',30000)

select * FROM trainees
select * FROM semester
select * FROM fee

--inner join- returns data that have matching values in both tables
SELECT trainees.admin_no,trainees.firstname,trainees.lastname,fee.course,fee.amount
FROM trainees
INNER JOIN fee ON trainees.admin_no = fee.admin_no

--joining 3 tables
SELECT trainees.admin_no,trainees.firstname,trainees.lastname,fee.course,fee.amount,semester.semName
FROM trainees
INNER JOIN fee ON trainees.admin_no = fee.admin_no
INNER JOIN semester ON semester.semNo = fee.semNo

--left Outer Join -- Returns data similar to inner join, but
--all the data from left table will be displayed even if no match
SELECT trainees.admin_no,trainees.firstname,trainees.lastname,fee.course,fee.amount
FROM trainees
LEFT OUTER JOIN fee ON trainees.admin_no = fee.admin_no

--right Outer Join -- Returns data similar to inner join, but
--all the data from right table will be displayed even if no match
SELECT trainees.admin_no,trainees.firstname,trainees.lastname,fee.course,fee.amount
FROM trainees
RIGHT OUTER JOIN fee ON trainees.admin_no = fee.admin_no

--Full Outer Join -- Returns data similar to inner join, but
--all the data from right as well as left table will be displayed even if no match
SELECT trainees.admin_no,trainees.firstname,trainees.lastname,fee.course,fee.amount
FROM trainees
FULL OUTER JOIN fee ON trainees.admin_no = fee.admin_no

--self join, to join the same table with different alias names
SELECT t1.firstname, t1.lastname,t2.city
FROM trainees t1,trainees t2
WHERE t1.admin_no = t2.admin_no
AND t1.city = t2.city
ORDER BY t2.city

--cross join (cartesian product)
SELECT * FROM trainees 
CROSS JOIN fee

--combining cross join with WHERE clause
SELECT trainees.admin_no,trainees.firstname,trainees.lastname,fee.course,fee.amount
FROM trainees
CROSS JOIN fee WHERE trainees.admin_no = fee.admin_no


----Stored Procedure----

CREATE PROCEDURE traineeAgewiseList
AS
BEGIN
	SELECT firstname, age, city
	FROM trainees
	ORDER BY age;
END;

--execute stored procedure
EXEC traineeAgewiseList

--altering stored procedure
ALTER PROCEDURE traineeAgewiseList
AS
BEGIN
	SELECT admin_no,firstname,age,city
	FROM trainees
	ORDER BY age;
END;

--list all stored procedures in current DB
SELECT * FROM sys.procedures

--removing  stored procedure
DROP PROCEDURE traineeAgewiseList

--passing parameters into stored procedures
CREATE PROCEDURE getTraineesFromCity(@city VARCHAR(50))
AS
BEGIN
	SET NOCOUNT ON;
	SELECT firstname,lastname,age,city
	FROM trainees
	WHERE city = @city
END
--executing the SP by passing parameters
EXEC getTraineesFromCity 'Texas'

--return parameter from stored procedure
CREATE PROCEDURE getTraineeCount(@traineeCount INT OUTPUT)
AS
BEGIN
	SELECT @traineeCount = COUNT(id) FROM trainees;
END

--receiving output from stored procedure
--step1 declare the variable to hold the output
DECLARE @TraineeCount INT
--step2 executing the stored procedure
EXEC getTraineeCount @TraineeCount OUTPUT
--step3 print the output variable
PRINT @traineeCount


--subquery in SELECT Clause
SELECT * FROM trainees
WHERE id IN(SELECT id FROM trainees WHERE age > 12)

--subquery in DELETE Clause
DELETE FROM trainees
	WHERE admin_no IN (SELECT admin_no FROM trainees WHERE admin_no = 3354)


	--creating a view
	CREATE VIEW [ny trainees] AS
	SELECT firstname,lastname, city
	FROM trainees WHERE city= 'New York'

	--query the view 
	SELECT * FROM [ny trainees]


--creating DDL trigger (for events of create,alter,drop)
CREATE TRIGGER dont_play_withmydb
ON DATABASE FOR create_table,alter_table,drop_table --ON db FOR events
AS -- trigger execution statements
print 'Not Allowed!! In My DB'
rollback; --roll back to previous state

--testing the trigger
CREATE TABLE testTable(
id int
);

--delete the trigger
DROP TRIGGER dont_play_withmydb ON DATABASE

--creating a DML trigger(for events of insert, update, delete)

CREATE TRIGGER msg_after_insert
ON trainees
AFTER INSERT AS
BEGIN
	PRINT 'inserted fine'
END

INSERT INTO trainees VALUES (3354, 'spider','man',10,'tvm')

--deleting the after DML trigger
DROP TRIGGER msg_after_insert

--creatinng the trainee backup table
create table trainee_backup(
    id int primary key identity,
    admission_no varchar(45) not null,
    first_name varchar(45) not null,
    last_name varchar(45) not null,
    age int,
    city varchar(25) not null
    );

--create an AFTER trigger which can backup data to another table
CREATE TRIGGER backup_trainees
ON trainees
AFTER INSERT
AS
BEGIN
	SET NOCOUNT ON; --to suppress the no. of affected rows message
	--declaring variables to hold the values temporarily
	DECLARE @id INT
	DECLARE @admin_no INT
	DECLARE @age INT
	DECLARE @firstname VARCHAR(45)
	DECLARE @lastname VARCHAR(45)
	DECLARE @city VARCHAR(45)
	SELECT @id = I.id,
	@admin_no = I.admin_no,
	@firstname = I.firstname,
	@lastname = I.lastname,
	@age = I.age,
	@city = I.city
	FROM INSERTED I
	INSERT INTO trainee_backup
	VALUES( @admin_no, @firstname,@lastname,@age,@city)
	PRINT ' Values inserted intp both trainee and backup tables'
END


INSERT INTO trainees(admin_no,firstname,lastname,age,city) VALUES
(3377,'spider','man',13,'texas')

--Instead trigger
CREATE TRIGGER do_insteadof_insert
ON trainees
INSTEAD OF INSERT
AS
BEGIN
	PRINT 'values are not inserted because of a trigger!!!'
END

