-- This script creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on your MySQL server with the attribute
-- id INT unique, auto generated, not null and state_id which is a foreign 
-- key that references to id of the states table and
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(
	id INT NOT NULL AUTO_INCREMENT,
        state_id INT NOT NULL, 	
	name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id),
	FOREIGN KEY(state_id) REFERENCES states(id)
);
