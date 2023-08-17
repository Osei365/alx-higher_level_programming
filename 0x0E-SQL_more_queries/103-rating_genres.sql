-- get ratings of genre

SELECT tv_genres.name AS name, SUM(tv_show_ratings.rate) AS rating
FROM tv_show_ratings 
LEFT JOIN tv_shows ON tv_shows.id = tv_show_ratings.show_id
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY name
ORDER BY rating DESC;
