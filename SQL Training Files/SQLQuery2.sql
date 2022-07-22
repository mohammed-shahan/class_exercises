-- To create new database
CREATE DATABASE employee_db1

-- list all databases in the server
SELECT name from master .sys.databases

--list all databases in the server order by name
SELECT name from master .sys.databases ORDER BY name;

--select the databases
USE employee_db

--to create the backup of the database
BACKUP DATABASE employee_db TO DISK = 'D:\employeedb_backup\employee_db.bak'

--to create the backup of the database
BACKUP DATABASE employee_db TO DISK = 'D:\employeedb_backup\employee_db.bak'
WITH DIFFERENTIAL

--delete database
DROP DATABASE employee_db

--restoring data dfrom the backup
RESTORE DATABASE employee_db
FROM DISK = 'D:\employeedb_backup\employee_db.bak'
WITH REPLACE

--find the default schema of the current database
SELECT SCHEMA_NAME()

--creating a scehma
CREATE SCHEMA myschema1

--creating a schema by explicitly specifying the user
CREATE SCHEMA myschema2 AUTHORIZATION dbo

-- creating a table and placing it under the myscehma1 schema
CREATE TABLE myschema1.mytable(
ID int,
FirstName nvarchar(50) NOT NULL,
LastName nvarchar(50) NOT NULL
)

--Remove the schema from the database
ALTER SCHEMA IF EXISTS myschema1

--transfer all the db objects under myschema1 to dbo schema
ALTER SCHEMA dbo
TRANSFER OBJECT::myschema1.mytable1