--Mohammed shahan


CREATE DATABASE company;
USE company;


-- creating sales table

CREATE TABLE sales (
	orderID INT IDENTITY PRIMARY KEY,
	ordDate DATE DEFAULT GETDATE(),
	ordPrice int,
	ordQty INT DEFAULT 1,
	custName VARCHAR(30) CHECK(custName IS NOT NULL),
	);


INSERT INTO sales VALUES 
	('2020-11-22', 190, 2, 'Sam'),
	('2020-07-10', 120, 2, 'Antony'),
	('2020-06-13', 350, 5, 'Teena'),
	('2020-06-13', 420, 2, 'Merin'),
	('2020-11-22', 700, 4, 'Jacob'),
	('2020-09-02', 650, 4, 'Lisa'),
	('2020-10-03', 1000, 2, 'Derick');


SELECT * FROM sales;


--Orders made by John
SELECT COUNT(orderID) FROM sales WHERE custName = 'Sam';



--number of unique customers

SELECT  COUNT(DISTINCT custName) FROM sales;



-- Total number of items ordered by all

SELECT SUM(ordQty) FROM sales;


--Average
SELECT AVG(ordQty) FROM sales;


--Average order quantity more than price 300
SELECT AVG(ordQty) FROM sales
WHERE ordPrice > 300;


-- Minimum price paid for any order

SELECT MIN(ordPrice) FROM sales;


--Customers name ends with 'n'

SELECT custName FROM sales 
WHERE custName LIKE '%n';


--All unique customer names

SELECT DISTINCT custName FROM sales;


--Total amount spent by each customer

SELECT custName,sum(ordPrice) AS Total FROM sales
GROUP BY custName


--Unique customers who spend more than 700

SELECT DISTINCT custName FROM sales WHERE ordPrice > 700;


--Customers ordered more than 3
SELECT custName,ordQty FROM sales WHERE ordQty>3;


--All those who spend more than 600

SELECT custName, ordPrice FROM sales WHERE ordPrice > 600;


--List of orders in ascending order of price

SELECT * FROM sales
ORDER BY ordPrice;


--List of orders in descending order of price

SELECT * FROM sales
ORDER BY ordPrice DESC;