-- lists the number of records with the same score in the second_table
-- result should display the score, number of records for this score
-- list should be sorted by the number of records (descending)
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score;
