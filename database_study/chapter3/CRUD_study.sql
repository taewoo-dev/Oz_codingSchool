-- create database mydatabase;
-- use mydatabase;
-- create table users (
-- 	user_id int primary key,
--     username text not null,
--     email text not null,
--     age int
-- );

-- insert into users (user_id,username, email, age)
-- values (1,"taewoo","123@naver.com",26),
-- 	   (2,"홍길동","1234@naver.com",27),
--        (3,"이길동","1235415@gmail.com",30),
-- 	   (4,"삼길동","x@andsa.com",32);

-- insert into users (user_id,username,email)
-- values (5,'사길동','123@gmail.com');

-- insert ignore into users (user_id,username,email,age) -- id까지 모두 동일한 레코드가 있을 경우 중복된 값은 추가하지 않는다.
-- values (3,"삼길동","x@andsa.com",32), -- 대신 같이 넣는 다른 값은 생성된다.
-- 	   (6,"오길동","12345@naver.com",33);
       
-- insert into users (user_id,username,email,age)
-- values (6,"오길동","12345@naver.com",33) 중복값이 존재한다면
-- on duplicate key update age = 50; -- 이 조건으로 value를 업데이트 ex) age 30->50
-- insert into users set user_id=7, username="육길동", email="길동@naver.com", age=10;

-- select * from users; -- 기본적인 데이터조회 
-- select age, age*100 as age100 from users; -- 원하는 열 가져오기
-- select age, age*100 from users; as로 별칭 붙이기

-- select * from users order by age;
-- select * from users order by username;
-- select user_id, email from users;
-- select * from users order by user_id desc;
-- select * from users order by age desc;
-- select * from users order by age asc, user_id desc; -- age로 1차 정렬, age가 같은 값은 user_id로 정렬

-- select * from users limit 5;
-- select * from users limit 3,4; -- limit 3,4 == str[3:7] 3번째 부터 4개 조회

-- select * from users where user_id = 3;
-- select * from users where age = 30 and user_id = 3;

-- select * from users where not user_id = 3;
-- select * from users where not age = 30;
-- select * from users where age between 10 and 27 order by age;
-- select user_id, count(*) as user_count from users group by user_id;
-- select -- case when 구문을 이용해서 조건에 맞춰 변환하여 조회한다
-- 	username,
--     age,
--     case when age >= 30 then "성인" else '미성년자' end as age_group from users;
-- select
--    username,
--    user_id,
--    case when user_id >= 5 then "upper" else "lower" end as round from user;

-- create table orders (
-- 	order_id int primary key auto_increment,
--     user_id int,
--     ordername text not null,
--     amount int not null,
--     foreign key (user_id) references users(user_id)
--     );

-- insert into orders (user_id, ordername, amount)
-- values (1,"taewoo",10000),
-- (3,"홍길동",20000);

-- select * from orders;

-- select users.username, users.age, orders.user_id 
-- from users  -- users로부터 orders와 조인하겠다. users.user_id(primary)와 orders.user_id(foreign key)
-- join orders on users.user_id = orders.user_id;

-- select
-- 	username,
--     age,
--     row_number() over (order by age desc) AS rank1
-- from users;

-- update users
-- set username = "일호"
-- where user_id = 1;

-- select username from users;

-- set sql_safe_updates = 0;
-- update users
-- set username = '아저씨'
-- where age >= 30;

-- select username from users;
-- select Row_count();

-- update users
-- set username = case
-- 	when age >= 30 then "으른"
--     else "으른이"
-- end;

-- select * from users;

-- update users
-- set username = "홍길동"
-- 	where age = 26
--     limit 3;

-- select * from users;

-- update users
-- set username = "어른"
-- where username = "으른이"
-- limit 2; 

-- delete from users; -- 조인되어 있는 하위 테이블이 있을 시 삭제가 안된다
       