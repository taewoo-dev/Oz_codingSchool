-- create table user (
-- 	user_id int primary key auto_increment,
--     password varchar(4),
--     name varchar(3),
--     gender ENUM('male','female'),
--     email varchar(15),
--     birthday CHAR(6),
--     age TINYINT,
--     company enum("samsung","lg","hyundai")
-- );

-- create table borad (
-- 	borad_id int primary key auto_increment,
--     title varchar(5),
--     content varchar(10),
--     likes int check (likes between 1 and 100),
--     created date,
--     user_id int,
--     foreign key (user_id) references user(user_id)
--     );
