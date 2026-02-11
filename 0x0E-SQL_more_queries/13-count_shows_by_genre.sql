-- This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Doesn't display a genre that doesn’t have any shows linked
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- First column is called genre
-- Second column is called number_of_shows
-- Results are sorted in descending order by the number of shows linked
SELECT tv_genres.name AS genre, COUNT(tv_shows.title) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
GROUP BY genre
ORDER BY number_of_shows DESC;
