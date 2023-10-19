-- To display all the cities of California from database hbtn_0d_usa
-- Displays rows of a column in a database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
