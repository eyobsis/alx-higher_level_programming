-- This creates a database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
-- creates a database step 01
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database step 02
USE hbtn_0d_usa;
-- creates a table final step query
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));
