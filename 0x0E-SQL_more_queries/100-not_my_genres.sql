-- This script uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
-- Each record displays: tv_genres.name.
-- Results are sorted in ascending order by the genre name.
SELECT name
FROM tv_genres
WHERE tv_genres.id NOT IN (SELECT genre_id
			   FROM tv_show_genres
			   WHERE tv_show_genres.show_id = (SELECT tv_shows.id
							   FROM tv_shows
							   WHERE tv_shows.title = 'Dexter'))
ORDER BY name;
