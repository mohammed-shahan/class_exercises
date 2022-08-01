CREATE DATABASE PatientMngmnt 

USE PatientMngmnt

CREATE TABLE patient (
    ptID INT PRIMARY KEY,
    ptName VARCHAR(20),
    ptgender VARCHAR(10),
    ptage INT,
    ptBloodGroup VARCHAR(4)
)

CREATE PROCEDURE addPatient (@ptID AS INT, @ptName AS VARCHAR(20), @ptgender AS VARCHAR(10), @ptage AS INT, @ptBloodGroup AS VARCHAR(4)) AS
BEGIN
    INSERT INTO patient VALUES (@ptID, @ptName, @ptgender, @ptage, @ptBloodGroup)
END

CREATE PROCEDURE updatePatient (@ptID AS INT, @ptName AS VARCHAR(20), @ptgender AS VARCHAR(10), @ptage AS INT, @ptBloodGroup AS VARCHAR(4)) AS
BEGIN
    DELETE FROM patient WHERE ptID = @ptID
    INSERT INTO patient VALUES (@ptID, @ptName, @ptgender, @ptage, @ptBloodGroup)
END

CREATE PROCEDURE deletePatient (@ptID AS INT) AS
BEGIN
    DELETE FROM patient WHERE ptID = @ptID
END

CREATE PROCEDURE listPatient AS
BEGIN
    SELECT * FROM patient
END

CREATE PROCEDURE searchPatient (@id AS INT) AS
BEGIN
    SELECT * FROM patient WHERE ptID=@id
END