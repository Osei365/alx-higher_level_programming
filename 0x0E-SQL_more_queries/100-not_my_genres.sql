-- selects names of genres not linked to Dexter

SELECT tv_genres.name AS name FROM tv_genres
WHERE name NOT IN
(SELECT tv_genres.name AS name FROM tv_show_genres
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter')
ORDER BY name;
