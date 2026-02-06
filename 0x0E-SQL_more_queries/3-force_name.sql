-- This script creates the table force_name on the database hbtn_0d_2 with a name attribute that can't be NULL.
CREATE TABLE IF NOT EXISTS force_name
(
	id	INT,
	name	VARCHAR(256) NOT NULL
);
