--Transactions
--Simple transaction example
--starting transactions example
BEGIN TRANSACTION
--The SQL statements to execute one by one
INSERT INTO semester VALUES (5,'sem 5') --query1
UPDATE semester SET semname = 's5' WHERE semno = 5 --query2
--commit changes and the transaction
COMMIT TRANSACTION


--manually rolling back the transactions
-- strating a transaction
BEGIN TRANSACTION
--The SQL statements to execute one by one
INSERT INTO semester VALUES (6,'sem 6')
UPDATE semester SET semname = 's6' WHERE semno = 6
--commit changes and the transaction
ROLLBACK TRANSACTION

select * from semester


--rolling back the transactions if there is error
-- strating a transaction
BEGIN TRANSACTION
--The SQL statements to execute one by one
INSERT INTO semester VALUES (6,'sem6')
UPDATE semester SET semname = 2 WHERE semno = 6
--checking if there is error usimg system variable @@ERROR
IF(@@ERROR > 0)
	BEGIN
		ROLLBACK TRANSACTION
	END
ELSE
	BEGIN
		COMMIT TRANSACTION
	END

