-- CREATE TABLE users(
-- 	user_id INT primary key auto_increment,
--     username varchar(100),
--     email varchar(100)
-- );

-- create table orders(
-- 	order_id int primary key auto_increment,
--     user_id int,
--     product_name varchar(100),
--     quantity int,
--     foreign key (user_id) references users(user_id)
-- );

-- select * from users -- left join은 기준이 되는 테이블은 다보여주고 조인당하는 테이블은 겹치는 부분만 출력
-- left join orders on users.user_id = orders.user_id; -- on 뒤에는 join 조건

-- select * from users -- 교집합 서로 겹치는 부분만 출력
-- inner join orders on users.user_id = orders.user_id; 
