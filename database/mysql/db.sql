drop database if exists db;
create database db;
use db;

create table course(
   id_course int not null auto_increment primary key,
   description varchar(50),
   price decimal(6,2),
   period varchar(20) default "matutino"
);

insert into course (id_course, description, price, period) values
(default, "Engenharia", 1000.00, default),
(default, "Agronomia", 1000.00, default),
(default, "Medicina", 1000.00, default),
(default, "Analise de Sistemas", 1000.00, default),
(default, "Fisioterapia", 1000.00, default);

create table student(
   id_student int not null auto_increment primary key,
   _name varchar(50),
   email varchar(50),
   address varchar(50),
   city varchar(20) default "Londrina",
   uf varchar(2) default "PR",
   id_course int not null default 2,
   foreign key (id_course) references course (id_course)
);

insert into student (id_student, _name, email, address, city, uf, id_course) values
(default, "Joazir", "joazir@email.com.br", "Av. Curitiba, nº35", default, default, 1),
(default, "Amarildo", "amarildo@email.com.br", "Av. Noronha, nº135", default, default, 3),
(default, "Bertram", "bertram@email.com.br", "Av. São Paulo, nº55", default, default, 4),
(default, "Natanael", "natanael@email.com.br", "Av. Ibati, nº12", default, default, 5),
(default, "Cicero", "cicero@email.com.br", "Av. Adão Nobre, nº265", default, default, 1);


-- QUERY
-- select * from student;
-- select * from course;


-- |||||||||||||||||||STUDENT||||||||||||||||||||| --
-- |CREATE|
-- insert into table_name (column1, column2, column3)
-- values (value1, value2, value3);
-- ---------------------------
-- insert into student (id_student, _name, email, address, city, uf, id_course) values
-- (default, "Joazir", "joazir@email.com.br", "Av. Curitiba, nº35", default, default, 1);

-- |READ|
-- select column1, column2, ...
-- from table_name;
-- ---------------------------
-- select concat('id: ',id_student,'    nome: ', _name)
-- from student order by _name;

-- |UPDATE|
-- update table_name
-- set column1 = value1, column2 = value2,
-- where condition;
-- ---------------------------
-- select * from student;
-- update student set 
-- _name = "João",
-- email = "joao@email.com",
-- address = "Jardim das Flores",
-- city = default,
-- uf = default,
-- id_course = default
-- where id_student = '2'; 

-- |DELLETE|
-- delete from table_name where condition;
-- ---------------------------
-- delete from student where id_student = 7 limit 1;

-- ###########################################################

-- |||||||||||||||||||COURSE||||||||||||||||||||| --
-- |CREATE|
-- insert into table_name (column1, column2, column3)
-- values (value1, value2, value3);
-- ---------------------------
-- insert into course (id_course, description, price, period) values
-- (default, "Engenharia", 1000.00, default);

-- |READ|
-- select column1, column2, ...
-- from table_name;
-- ---------------------------
-- select id_course, description from course order by description;

-- |UPDATE|
-- update table_name
-- set column1 = value1, column2 = value2,
-- where condition;
-- ---------------------------
-- update course set description = "Artes" where id_course = 1; 


-- |DELLETE|
-- delete from table_name where condition;
-- ---------------------------
-- delete from course where id_course = 2 limit 1;

