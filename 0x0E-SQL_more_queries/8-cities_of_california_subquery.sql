-- lists all the cities of California found in the db hbtn_0d_usa
SELECT C.id, C.name FROM cities C, states S
WHERE C.state_id = S.id AND S.name = 'California'
ORDER BY C.id ASC;
