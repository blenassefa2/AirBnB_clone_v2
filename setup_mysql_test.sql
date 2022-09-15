-- Configuration of database for work

-- Create database named hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user of the database
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';

-- set password to user
SET PASSWORD FOR 'hbnb_test'@'localhost' = PASSWORD('hbnb_test_pwd');

-- give all the user's properties to the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- let the user see the perfomance data
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- avoid any errors by other user privileges
FLUSH PRIVILEGES;