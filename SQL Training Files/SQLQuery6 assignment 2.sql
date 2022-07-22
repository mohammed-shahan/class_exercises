USE employee_db

--creating table customer
CREATE TABLE customer(
	Customer_ID INT  PRIMARY KEY,
	Cust_Name varchar(50),
	City varchar(10),
	Grade SMALLINT,
	Sales_Amount INT,
	);

--inserting column values
INSERT INTO customer
VALUES(3002,'Anna','New York',100,5001),
	(3007,'Samanatha','New York',200,4001),
	(3005,'Jacob','California',200,2002),
	(3008,'Sophie','London',300,6002),
	(3004,'Joe','Paris',300,9000);

--listing table
SELECT * FROM customer

--highest and lowest graded customers
SELECT * FROM customer 
WHERE
Grade = (SELECT MIN(Grade) FROM customer);


SELECT * FROM customer 
WHERE
Grade = (SELECT MAX(Grade) FROM customer);


-- Average sales amount
SELECT AVG(Sales_Amount) AS 'Avg Sales Amount' FROM customer

--Total sales amount
SELECT SUM(Sales_Amount) AS 'Total Sales Amount'
FROM customer




		