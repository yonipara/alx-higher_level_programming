-- This script creates the table id_not_null on the given database as an argument with an id attribute that has a default value 1.
CREATE TABLE IF NOT EXISTS id_not_null
(
	id	INT DEFAULT 1,
	name	VARCHAR(256) NOT NULL
);
