select name, year_of_release from albums a
where year_of_release = 2018

select name, duration from songs order by duration desc limit 1

select name, duration from songs
where duration >='3:5'

select * from collection
where year_of_release between 2018 and 2020

select * from singer
where name not like '% %'

select * from songs
where name like '%мой%' or name like '%my%'

