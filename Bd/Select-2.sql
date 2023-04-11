select g.name, count(si.singer_id) as singer_count from genres g
left join genres_singer gs on g.genres_id = gs.genres_id
left join singer si on gs.singer_id = si.singer_id
group by g.name

select count(*) from songs s 
join albums a on s.album=a.albums_id 
where a.year_of_release BETWEEN 2019 AND 2021

select distinct s.name
from singer s
left join singer_albums sa on s.singer_id = sa.singer_id
left join songs on sa.singer_id = songs.songs_id
left join albums al on songs.album = al.albums_id
where al.year_of_release != 2020 or al.year_of_release IS null

select c.name, s2.name
from collection c
join collection_songs cs on c.collection_id = cs.collection_id
join songs s  on cs.songs_id = s.songs_id
join albums a2 on s.songs_id = a2.albums_id
join singer_albums sa on a2.albums_id = sa.albums_id
join singer s2 on sa.singer_id = s2.singer_id  
where s2.name = 'Eminem'

select distinct a.name
from albums a
join singer_albums sa on a.albums_id = sa.albums_id
join genres_singer gs on sa.singer_id = gs.singer_id 
group by a.name 
having count(distinct gs.genres_id)>1

select s.name
from songs s
left join collection_songs cs on s.songs_id = cs.songs_id 
where cs.collection_id is notnull 

select singer.name
from songs s 
join singer_albums sa on s.album = sa.albums_id 
join singer on sa.singer_id = singer.singer_id 
where s.duration = (select min(duration)
from songs)

select a.name
from albums a 
left join songs on a.albums_id = songs.album 
group by a.name
order by count(songs.songs_id)
limit 1