-- selects all shows without comedy genre

SELECT tv_shows.title AS title FROM tv_shows
WHERE title NOT IN
(SELECT tv_shows.title AS title FROM tv_show_genres
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy')
ORDER BY title;
