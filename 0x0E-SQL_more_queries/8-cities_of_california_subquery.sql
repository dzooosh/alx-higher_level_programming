-- lists all the cities of California found in the db hbtn_0d_usa
SELECT cities.id, states.name FROM cities C, states S
WHERE C.id = S.id
WHERE name = California
ORDER BY C.id;
