-- 1. 생성
-- (1) customers 테이블에 새 고객을 추가하세요.

-- INSERT INTO customers (customerNumber, customerName, phone, city)
-- VALUES (499,'taewoo', '010-1234-6423', 'seoul');

-- (2) products 테이블에 새 제품을 추가하세요.
-- INSERT INTO products (productCode, productName)
-- VALUES ('S700_31690','아이폰');

-- (3) **`employees`** 테이블에 새 직원을 추가하세요.

-- INSERT INTO employees (employeeNumber, email, reportsTo)
-- VALUES (1705, 'ab234@naver.com' , 1102);

-- (4) **`offices`** 테이블에 새 사무실을 추가하세요.

-- INSERT INTO offices (officesCode, city, phone)
-- values (8, 'seoul', '010-1234-1234');

-- (5) **`orders`** 테이블에 새 주문을 추가하세요.

-- INSERT INTO orders (orderNumber, orderDate, status)
-- VALUES (10426, '2024-01-01', 'Shipped')

-- (6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요.

-- INSERT INTO orderdetails (orderNumber, productCode, priceEach)
-- VALUES (10205, 'S10_4757' , 140);

-- (7) **`payments`** 테이블에 지불 정보를 추가하세요.

-- select * from payments;
-- insert into payments (customerNumber, checkNumber, amount)
-- values (497, "QM333124", 60000);

-- (8) **`productlines`** 테이블에 제품 라인을 추가하세요.

-- insert into productlines (productLine, textDescription)
-- values ('아이폰', 'qweqwe');

-- (9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.

-- insert into customers (customerNumber, city)
-- values (500,'seoul');

-- (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
-- select * from prouducts;
-- INSERT INTO products (productCode, productName, buyprice, productLine) 
-- VALUES ("S18_2000",'Vi train', 50, 'Trains');

-- 2. 읽기
-- (1) **`customers`** 테이블에서 모든 고객 정보를 조회하세요.
-- select * from customers;

-- (2) **`products`** 테이블에서 모든 제품 목록을 조회하세요.
-- select * from products;

-- (3) **`employees`** 테이블에서 모든 직원의 이름과 직급을 조회하세요.
-- select * from employees;

-- (4) **`offices`** 테이블에서 모든 사무실의 위치를 조회하세요.
-- select * from offices;

-- (5) **`orders`** 테이블에서 최근 10개의 주문을 조회하세요.
-- select * from orders;

-- (6) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
-- select * from orderdetails;

-- (7) **`payments`** 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
-- select * from payments;

-- (8) **`productlines`** 테이블에서 각 제품 라인의 설명을 조회하세요.
-- select * from productlines;

-- (9) **`customers`** 테이블에서 특정 지역의 고객을 조회하세요.
-- select * from customers;

-- (10) **`products`** 테이블에서 특정 가격 범위의 제품을 조회하세요.
-- select * from products;

-- 3.갱신
-- (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
-- UPDATE customers SET addressLine1 = '업데이트' WHERE customerNumber = 1;

-- (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
-- select * from products;
-- SET SQL_SAFE_UPDATES = 0;
-- UPDATE products set buyPrice = 50 WHERE (productName = "The Titanic");

-- (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
-- select * from employees;
-- UPDATE employees set jobTitle = "Sales Manager" where employeeNumber = 1088;


-- (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
-- select * from offices;
-- update offices set phone = 02-1234-1234 Where city = "Tokyo";

-- (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
-- select * from orders;
-- update orders set status = "On Hold" where orderNumber = 10333;

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
-- select * from orderdetails;
-- update orderdetails set quantityOrdered = 50 where orderNumber = 1;

-- (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
-- select * from payments; 
-- update payments set amount = 7000 where customerNumber = 112;

-- (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
-- select * from productlines;
-- update productlines set textDescription = "내가 변경" where productLine = "Ships";

-- (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.
-- select * from customers;
-- update customers set customerName = "abc@naver.com" where customerNumber = 103;

-- 4. 삭제
-- (1) **`customers`** 테이블에서 특정 고객을 삭제하세요.
-- DELETE FROM customers WHERE customerNumber = 1;

-- (2) **`products`** 테이블에서 특정 제품을 삭제하세요.
-- select * from products;
-- DELETE FROM products WHERE productLine = "Ships";

-- (3) **`employees`** 테이블에서 특정 직원을 삭제하세요.
-- select * from employees;
-- DELETE FROM employees WHERE lastname = "Murphy";

-- (4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.
-- select * from offices;
-- DELETE FROM offices WHERE officeCode = 1;

-- (5) **`orders`** 테이블에서 특정 주문을 삭제하세요.
-- select * from orders;
-- DELETE FROM orders WHERE orderNumber = 10100;

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.
-- select * from orderdetails;
-- DELETE FROM orderdetails WHERE priceEach = 136.00;

-- (7) **`payments`** 테이블에서 특정 지불 내역을 삭제하세요.
-- select * from payments;
-- DELETE FROM payments where customerNumber = 103;

-- (8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.
-- select * from productlines;
-- DELETE FROM productlines where productLine = "아이폰";

-- (9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.
-- TRUNCATE customers;

-- (10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
-- TRUNCATE products;