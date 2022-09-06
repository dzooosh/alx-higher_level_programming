-- lists all records with a score >= 10 in the second_table
-- of the database hbtn_0c_0 in your mysql server
-- results should display both the score and the name
-- records should be ordered by score (top first)
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
