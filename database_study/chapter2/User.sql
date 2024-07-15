-- CREATE DATABASE mydatabase; -- mydatabase라는 이름을 가진 데이터 베이스를 생성
-- SHOW databases; -- 모든 데이터베이스 조회
-- use mydatabase; -- mydatabase 사용
-- DROP DATABASE IF exists mydatabase; -- mydatabase 삭제
-- CREATE USER "taewoo"@"localhost" IDENTIFIED BY '12345678'; -- 새로운 사용자 생성 및 비밀번호 설정

-- USE mysql -- mysql 데이터베이스를 사용
-- SELECT * FROM user; --모든 사용자 조회
-- SET PASSWORD FOR 'taewoo'@'localhost' = '1234'; -- 사용자 비밀번호 변경
-- GRANT ALL privileges ON *.* TO 'taewoo'@'localhost'; -- 사용자에게 모든 권한 부여
-- SHOW GRANTS FOR 'taewoo'@'localhost'; -- taewoo 사용자의 권한 출력
-- SHOW GRANTS; -- root 사용자의 권한 출력
-- Drop USER 'taewoo'@'localhost' -- 사용자 삭제

-- 테이블 생성
CREATE TABLE users (
-- 스키마 : 사용자 데이터의 유효성 검사를 위한 데이터 제한
	id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    is_business VARCHAR(10) DEFAULT False,
    age INT CHECK (age>=18)
);

-- 데이터 삽입 
INSERT INTO users (username, email, age) VALUES
("이길동", "abcdnaver.com",22);

-- 데이터 조회
SELECT * FROM users
