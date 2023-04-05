insert into genres(name)
values('pop'),('rock'),('classiс'),('rap'),('chanson')

insert into singer(name)
values('Юра Шатунов'),('MIA BOYKA'),('Король и шут'),('Eminem'),('Sinitana'),('Петлюра'),('Баста'), ('Ария')

update singer
set name='Тимати'
where singer_id = 7

insert into genres_singer(singer_id, genres_id)
values(1, 1), (2, 1), (3, 2), (4, 4), (5, 3), (6, 5), (7, 4), (8, 2)

insert into albums(name, year_of_release)
values('Седая ночь', 2002), ('Прощальный альбом', 2021), ('Ели мясо мужики', 1999), ('Encore', 2004), ('In silence', 2016), ('Малолетка', 1995), ('Black star', 2006), ('Через все времена', 2014)

insert into singer_albums
values(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)

insert into songs(name, duration, album)
values('Седая ночь', '5:35', 1), ('Фенечка', '3:48', 1)

insert into songs(name, duration, album)
values('Танцы под дождем', '2:04', 2), ('Ауф', '1:35', 2)

insert into songs(name, duration, album)
values('Ели мясо мужики', '2:40', 3), ('Охотник', '2:44', 3)

insert into songs(name, duration, album)
values('Evil deeds', '4:20', 4), ('Mosh', '5:18', 4)

insert into songs(name, duration, album)
values('In silence', '3:19', 5), ('In silence(Extended mix)', '7:05', 5)

insert into songs(name, duration, album)
values('Бродяга', '2:45', 6), ('Стена', '3:46', 6)

insert into songs(name, duration, album)
values('Детка', '4:22', 7), ('Вопросы', '4:24', 7)

insert into songs(name, duration, album)
values('Город', '7:12', 8), ('Через все времена', '5:42', 8)


insert into collection (name, year_of_release)
values('Хиты', 2010), ('Новые хиты', 2012), ('Хиты еще новее', 2014), ('Самые новые хиты', 2016), ('Обновленные хиты', 2018), ('Абсолютно новые хиты', 2020), ('Старые хиты', 2022), ('Хиты перезагрузка', 2023)

insert into collection_songs (songs_id, collection_id)
values(1, 1), (2, 1), (3, 2), (4, 2), (5, 2), (1,5), (6, 8), (7, 7), (8, 6), (9, 4), (10, 6), (12, 2)

select * from songs s 