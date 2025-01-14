-- Configuration of database for work

-- Create database named hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- use the database
USE `hbnb_test_db`;

-- Create user of the database
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- give all the user's properties to the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- let the user see the perfomance data
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
