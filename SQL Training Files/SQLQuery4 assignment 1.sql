SELECT name from master .sys.databases

CREATE DATABASE hospital_db

USE hospital_db

BACKUP DATABASE hospital_db TO DISK = 'D:\employeedb_backup\hospital_db.bak'

USE master

DROP DATABASE hospital_db

RESTORE DATABASE hospital_db
FROM DISK = 'D:\employeedb_backup\hospital_db.bak'
WITH REPLACE
