-- Lists all records of the table second_table and a name value in myDB.
-- which are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
