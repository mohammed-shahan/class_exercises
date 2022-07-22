--WHERE CLAUSE EXAMPLESs
--WHERE WITH and BETWEEN
SELECT CompanyName, city, Country
	FROM Suppliers
	WHERE Country= 'USA'
	ORDER BY CompanyName;

SELECT * FROM employees
	WHERE employeeID BETWEEN 1 AND 5

--IN and LIKE operator with WHERE clause
SELECT * FROM employees 
	WHERE employeeID IN (1,2,3)

SELECT * FROM employees
	WHERE FirstName LIKE 'Robert'

--Order by clause 
SELECT FirstName, BirthDate FROM employees
	ORDER BY Birthdate DESC

SELECT FirstName, BirthDate FROM employees
	ORDER BY Birthdate DESC, Firstname ASC;

--having clause
--like the WHERE clause, but can be used along with aggregate functions
SELECT ProductName FROM Products
	GROUP BY ProductName, UnitPrice
	HAVING AVG(UnitPrice)>20

--SELECT clause examples
SELECT * FROM Products
SELECT ProductName, UnitPrice FROM Products

--eg of combining concat operation with select statement
SELECT CONCAT(LastName,'-',FirstName) AS FullName FROM employees




------------------
USE employee_db

CREATE TABLE EmployeeMaster
(
	Id INT IDENTITY PRIMARY KEY,
	EmployeeCode VARCHAR(10),
	EmployeeName VARCHAR(25),
	DepartmentCode VARCHAR(10),
	LocationCode VARCHAR(10),
	Salary INT
	)


INSERT INTO EmployeeMaster VALUES
('E0001', 'Hulk', 'IT', 'TVM', 4000),
('E0002', 'Spiderman', 'IT', 'TVM', 4000),
('E0003', 'Ironman', 'QA', 'KLM', 3000),
('E0004', 'Superman', 'QA', 'KLM', 3000),
('E0005', 'Batman', 'HR', 'TVM', 5000),
('E0006', 'Raju', 'HR', 'KTM', 5000),
('E0007','Radha', 'HR', 'KTM', 5000)

SELECT * FROM employeemaster


--Grouping SET examples
select EmployeeCode, EmployeeName, DepartmentCode, LocationCode,
SUM(Salary) as TotalCost
from EmployeeMaster
group by
    grouping sets
        (
            (EmployeeCode, EmployeeName, DepartmentCode, LocationCode),
            (DepartmentCode),
            (LocationCode),
            ()
            );
--IN and NOT operators
select * from EmployeeMaster where Salary IN (3000,5000)
select * from EmployeeMaster where EmployeeName not IN ('Raj','spidey')

-- btw ,null opereators

select * from EmployeeMaster where Salary between 3000 and 5000
select * from EmployeeMaster where Salary is null

--LIKE operator
SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'SuperMan'

SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'Sup%'

SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE '%Man'

SELECT * FROM EmployeeMaster WHERE EmployeeName NOT LIKE '%Man'

SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE '%ra%'

SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'Su[pj]erMan%'

SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'Ra[nj]u%'

SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'Ra[^nj]u%'

----------------------------

CREATE TABLE EmployeeMaster2(
    Id INT IDENTITY PRIMARY KEY,
    EmployeeCode VARCHAR (10),
    EmployeeName VARCHAR (25),
    DepartmentCode VARCHAR (10),
    LocationCode VARCHAR (10),
    Salary INT
);


--union operator example
SELECT * FROM employeemaster
UNION
SELECT * FROM EmployeeMaster2

SELECT * FROM employeemaster
UNION ALL --gets all the duplicates also
SELECT * FROM EmployeeMaster2

SELECT employeename, salary FROM EmployeeMaster
	WHERE salary > 3000
	SELECT employeename, salary FROM employeemaster2

--a sample table to demonstrate popular data types
CREATE TABLE data_types_eg(
	bit_col BIT,
	char_col CHAR(3),
	date_col DATE,
	date_time_col DATETIME2(3),
	date_time_offset_col DATETIMEOFFSET(2),
	dec_col DECIMAL(4,2),
	num_col NUMERIC(4,2),
	bigint_col BIGINT,
	int_col INT,
	smallint_col SMALLINT,
	tinyint_col TINYINT,
	nchar_col NCHAR(10),
	time_col TIME(0),
	varchar_col VARCHAR(10) )


insert into data_types_eg values(
    1,
    'abc',
    '2022-07-08',
    '2022-07-08 12:47:50',
    '2022-07-08 12:47:50 +05:30',
    10.21,
    20.21,
    17777234782379,
    123245235,
    3773,
    233,
    N'नमस्ते',
    '12:51:30',
    'hello');

	

---------------------------
--primary key constraint
--setting primary key for a single column
CREATE TABLE usage_logs(
    logid INT NOT NULL IDENTITY PRIMARY KEY,
    message char(255) NOT NULL
)

--setup primary key for multiple columns

CREATE TABLE customer_orders (
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    UnitPrice INT,
    PRIMARY KEY (OrderID, ProductID)
)

--altering table to include primary key later
CREATE TABLE cricketers(
	cricketer_id INT NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	salary MONEY
	);

ALTER TABLE cricketers ADD CONSTRAINT
crick_id_pk PRIMARY KEY (cricketer_id)

--to view primary key ID
EXEC sp_help cricketers

--disable a primary key
ALTER INDEX crick_id_pk ON cricketers DISABLE;

--enable a primary key
ALTER INDEX crick_id_pk ON cricketers REBUILD;

--drop / delete primary key
ALTER TABLE cricketers
	DROP CONSTRAINT crick_id_pk
---------------------------------------
--create a foreign key
--creating a table with primary key
CREATE TABLE myproducts(
	product_id INT NOT NULL IDENTITY,
	product_name VARCHAR(50) NOT NULL,
	category VARCHAR(25)
	CONSTRAINT myproducts_pk PRIMARY KEY(product_id, product_name))
	
	--create a table  with two foreign keys which refer the two primary keys
	CREATE TABLE myinventory(
		inventory_id INT PRIMARY KEY,
		product_id INT NOT NULL,
		product_name VARCHAR(50) NOT NULL,
		CONSTRAINT fk_myinventory
			FOREIGN KEY(product_id, product_name)
			REFERENCES myproducts(product_id, product_name))

	--enable / disable Foreign key
	ALTER TABLE myinventory
		CHECK CONSTRAINT fk_myinventory

	ALTER TABLE myinventory
		NOCHECK CONSTRAINT fk_myinventory

--Drop the foreign key
ALTER TABLE myinventory
	DROP CONSTRAINT fk_myinventory

INSERT INTO usage_logs VALUES
(NULL)

--remove constraints
ALTER TABLE usage_logs
ALTER COLUMN message
CHAR(200) NOT NULL;

TRUNCATE TABLE usage_logs

--unique CONSTRAINT
--set UNIQUE CONSTRAINT during table creation
CREATE TABLE usage_logs(
	logid INT UNIQUE
	message char(250)
	)

	INSERT INTO usage_logs VALUES
	(NULL, 'test')

--remove unique constraint from the table
ALTER TABLE usage_logs
	DROP CONSTRAINT UQ_usage_lo_879565ed6656855

--add UNIQUE CONSTRAINT to the table
ALTER TABLE usage_logs
	ADD CONSTRAINT uniq_constraint
	UNIQUE (logid)

--check constraint at the table creation
CREATE TABLE usage_logs(
	logid INT NOT NULL UNIQUE CHECK (logid>10)
	message char(250)
	)




---------------------------
--Default Constraint
--at the time of table creation
CREATE TABLE usage_log(
logid INT NOT NULL UNIQUE,
message CHAR(250),
msgdate DATETIME NOT NULL DEFAULT GETDATE())

INSERT INTO usage_log (logid,message) VALUES 
(2,'test')

SELECT * FROM usage_logs

ALTER TABLE usage_log
	ADD CONSTRAINT def_date
	DEFAULT (GETDATE()) FOR msgdate

ALTER TABLE usage_log
	DROP CONSTRAINT def_date