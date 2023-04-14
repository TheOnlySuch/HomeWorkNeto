select g.name, count(si.singer_id) as singer_count from genres g
left join genres_singer gs on g.genres_id = gs.genres_id
left join singer si on gs.singer_id = si.singer_id
group by g.name;

select count(*) from songs s 
join albums a on s.album=a.albums_id 
where a.year_of_release BETWEEN 2019 AND 2021;

SELECT a."name" , AVG(s.duration)
FROM songs s
JOIN albums a  ON s.album  = a.albums_id
GROUP BY a.name;

SELECT name
FROM singer s
WHERE name NOT IN (
    SELECT distinct s.name
    FROM singer s2 
    JOIN singer_albums sa  ON s2.singer_id  = sa.singer_id
    JOIN albums a ON a.albums_id = sa.albums_id
    WHERE a.year_of_release  = 2020
);

select c.name, s2.name
from collection c
join collection_songs cs on c.collection_id = cs.collection_id
join songs s  on cs.songs_id = s.songs_id
join albums a2 on s.songs_id = a2.albums_id
join singer_albums sa on a2.albums_id = sa.albums_id
join singer s2 on sa.singer_id = s2.singer_id  
where s2.name = 'Eminem';

SELECT DISTINCT a.name
FROM albums a 
JOIN singer_albums sa  ON a.albums_id  = sa.albums_id
JOIN genres_singer gs  ON sa.singer_id  = gs.singer_id
GROUP BY a.albums_id , gs.singer_id
HAVING COUNT(gs.genres_id) > 1;

select s.name
from songs s
left join collection_songs cs on s.songs_id = cs.songs_id 
where cs.collection_id is not null;

select singer.name
from songs s 
join singer_albums sa on s.album = sa.albums_id 
join singer on sa.singer_id = singer.singer_id 
where s.duration = (select min(duration)
from songs);

SELECT albums.name
FROM albums JOIN songs ON albums.albums_id  = songs.album
GROUP BY albums.albums_id
HAVING COUNT(songs.songs_id) = (
    SELECT COUNT(songs.songs_id) FROM songs
    GROUP BY albums.albums_id
    ORDER BY 1 
    LIMIT 1
);
