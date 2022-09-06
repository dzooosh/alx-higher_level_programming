-- lists all the records of the second_table
-- of the database hbtn_0c_0 in mysql server
-- results should display both score and the name (in this order)
-- records should be ordered by score (top first)
USE hbtn_0c_0;
SELECT score, name FROM second_table 
ORDER BY score DESC;
