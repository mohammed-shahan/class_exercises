--Mohammed Shahan
--Assignment 2




create database emp;
use emp;
create table employee(
	 empNo int primary key
	,managerId int not null
	,firstName varchar(25)
	,lastName varchar(25)
	,userId int not null
	,deptNo int not null
	,salary money
	,commission money
	,joinDate date
	,designation varchar(10)
);

create table department(
	 deptNo int primary key
	,deptName varchar(25)
	,location varchar(25)
);
--The two tables are related by the primary key (deptno in Department table) and foreign key (deptno in the Employee table) ER Model for this problem
alter table employee 
add foreign key(deptNo) references department(deptNo); 

exec sp_help employee;

--Details of department is grouped together to form the department table
insert into department(deptNo,deptName,location)
values
	 (10,'CS','north')
	,(11,'ME','east')
	,(12,'Civil','south')
	,(13,'EC','west');
select * from department;

--Details of employees in the Employee Table.
insert into employee
values
	 (0,20,'Avent','Suresh',30,10,50000,1000,'2022-07-12','SE')
	,(1,21,'Bineesh','PB',31,11,60000,2000,'2022-07-12','ASE')
	,(2,22,'Catherine','Fernandes',32,10,70000,3000,'2022-07-12','ASE')
	,(3,22,'Don','Wiscow',33,12,60000,2000,'2022-07-12','SE');
select * from employee;

--Modify the Employee table structure to add the HRA component width 5 and 2 decimal places.
alter table employee add hra decimal(5,2);
update employee
set hra=10.11
where empNo=0;
update employee
set hra=10.12
where empNo=1;
update employee
set hra=10.13
where empNo=2;
update employee
set hra=10.14
where empNo=3;

select * from employee;

--HRA and PF component has to be added to the salary of all the employees. Add PF of width 5 and
--2 decimal places to the Employee table and add a constraint to the field that the value of the PF
--should not be greater than 5000.

alter table employee add pf decimal(5,2);
alter table employee add check(pf <= 5000);
update employee
set pf=10.00
where empNo=0;
update employee
set pf=100.00
where empNo=1;
update employee
set pf=200.00
where empNo=2;
update employee
set pf=300.00
where empNo=3;

select * from employee;

update employee set salary =salary+ hra;
update employee set salary =salary+pf;

--Retrieve the details of all employees sorted in the alphabetical order of their name
select * from employee
order by firstName asc

-- Display the details of the employee in the descending order of the income.
select * from employee
order by salary desc

--Display the details of all employees whose name starts with ‘A’ has ‘e’ in it and ends with ‘t’.
select * from employee
WHERE firstName LIKE 'A%e%t';

--Display the details of all employees who joined after ’01-Jan-98’ and whose salary is higher than 25000
select * from Employee
where joinDate >'01/01/1998' AND salary > 25000;




-----------------------------------------





--Creating CUstomer table
CREATE TABLE Customer(
	Custno INT PRIMARY KEY,
	Custname VARCHAR(20),
	Address VARCHAR(40)
);

--Creating Orders table
CREATE TABLE Orders(
	 orderno INT PRIMARY KEY
	,custno INT
	,orderdate date
	,CONSTRAINT fk_custno FOREIGN KEY(custno) REFERENCES Customer(Custno)
);

--Creating OrderItem table
CREATE TABLE OrderItem(
	 ItemID INT PRIMARY KEY
	,OrderNo INT
	,ItemName VARCHAR(20)
	,Quantity INT
	,CONSTRAINT fk_orderno FOREIGN KEY(OrderNo) REFERENCES Orders(orderno)
);
