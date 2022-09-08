-- lists all shows contained in a db with at least one linked
SELECT s.title, g.genre_id FROM tv_shows s 
INNER JOIN tv_show_genres g 
ON s.id = g.show_id 
ORDER BY 
s.title ASC,
g.genre_id ASC;
