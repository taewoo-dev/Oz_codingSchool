-- 과제 1번 사용자 생성 후 권한 부여하기
USE mysql;
SELECT * FROM USER;
CREATE USER 'fish_bread_user'@'localhost' IDENTIFIED BY "1234";
DROP USER 'testID'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'fish_bread_user'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS;
SHOW GRANTS FOR 'fish_bread_user'@'localhost';

-- 과제 2번 데이터베이스와 테이블 생성

CREATE DATABASE fishbread_db;
USE fishbread_db;

CREATE TABLE users (
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) UNIQUE,
    is_business VARCHAR(10) DEFAULT False

);

CREATE TABLE orders (
	order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    FOREIGN KEY (user_id)
    REFERENCES users(user_id) ON UPDATE CASCADE,
    order_date DATE,
    amount DECIMAL(10,2)
);

CREATE TABLE inventory (
	item_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(255) NOT NULL,
	quantity INT NOT NULL
);

CREATE TABLE sales (
	sale_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    FOREIGN KEY (order_id)
    REFERENCES orders(order_id) ON UPDATE CASCADE,
    item_id INT,
    FOREIGN KEY (item_id)
    REFERENCES inventory(item_id) ON UPDATE CASCADE,
    quantity_sold INT NOT NULL
); 

CREATE TABLE daily_sales (
	date DATE PRIMARY KEY,
    total_sales DECIMAL(10,2) NOT NULL
);