--Selecting database
USE hospital_db

--creating table patient
CREATE TABLE patient(
	Record_No INT IDENTITY PRIMARY KEY,
	Patient_Name varchar(50),
	Phone_no INT,
	Gender varchar(10),
	Age SMALLINT,
	location varchar(50)
	);

--altering table columns
ALTER TABLE patient
ADD Doctore_name varchar(50);

--inserting column values
INSERT INTO patient 
VALUES('Tom',29655,'Male',25,'Canada','SAM'),
		('Jerry',5454,'Male',35,'USA','SAM'),
		('Eric',5769,'Male',46,'USA','SAM');

--display the rows of the table
SELECT * FROM patient

--update data in the table
UPDATE patient
SET Patient_Name = 'Jack'
WHERE Patient_Name = 'Eric';

-- delete record from the table
DELETE FROM patient
WHERE name = 'Jerry'






USE Northwind

SELECT * FROM Products

--aggregate functions
--MIN
SELECT MIN(UnitPrice) AS 'Min Price' FROM Products

--MAX
SELECT MAX(UnitPrice) AS 'Max Price' FROM Products

--using aggregate function as subquery
SELECT ProductID, ProductName, UnitPrice FROM products 
WHERE
UnitPrice = (SELECT MIN(UnitPrice) FROM Products);

SELECT ProductID, ProductName, UnitPrice FROM products 
WHERE
UnitPrice = (SELECT MAX(UnitPrice) FROM Products);

SELECT AVG(UnitPrice) AS 'Avg Product Price' FROM Products

--To get the list of tables in the selected databse
SELECT * FROM Sys.tables

--sum aggregate function
SELECT SUM(UnitsInStock) AS 'Total Stock'
FROM Products

SELECT SUM(UnitsInStock) AS 'Total Stock'
FROM Products
WHERE Discontinued = 0

--count aggregate function
SELECT COUNT(ProductID) AS 'Product Count'
FROM Products

--------------------------------------------------------

--clauses in SQL
--DISTINCT CLAUSE
SELECT DISTINCT city FROM Customers

SELECT DISTINCT city, region FROM Customers

SELECT DISTINCT city, region FROM Customers
WHERE country = 'USA'

--Group by clause
SELECT COUNT(CustomerID) AS 'No. of Customers', country
FROM customers
GROUP BY country;

