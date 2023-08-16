-- counts shows of genres

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_rows
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_rows DESC;
