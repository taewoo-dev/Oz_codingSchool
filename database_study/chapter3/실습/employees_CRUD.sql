-- USE mydatabase;

-- 1. employees 테이블을 생성해주세요.
-- CREATE TABLE employees (
-- 	id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(100) NOT NULL,
--     position VARCHAR(100) NOT NULL,
--     salary DECIMAL(10,2)
-- );

-- 2. 직원 데이터를 employees에 추가해주세요.
-- INSERT INTO employees (name,position,salary)
-- VALUES ("혜린", "PM", 90000),
-- 	   ("은우", "Frontend", 80000),
--        ("가을", "Backend", 92000),
--        ("지수", "Frontend", 78000),
--        ("민혁", "Frontend", 96000),
--        ("하온", "Backend", 130000);

-- 3. 모든 직원의 이름과 연봉 정보만을 조회하는 쿼리를 작성해주세요.
-- SELECT name, salary from employees;

-- 4. Frontend 직책을 가진 직원중에서 연봉이 90000 이하인 직원의 이름과 연봉을 조회하세요.
-- SELECT name, salary from employees where position = "Frontend" and salary <= 90000;

-- 5. PM 직책을 가진 모든 직원의 연봉을 10% 인상한 후 그 결과를 확인하세요.
-- UPDATE employees
-- SET salary = salary*1.1
-- where position = "PM";

-- 6. 모든 Backend 직책을 가진 직원의 연봉을 5% 인상하세요.
-- UPDATE employees
-- SET salary = salary*1.05
-- WHERE position = "Backend";
-- SELECT * from employees;

-- 7. 민혁 사원의 데이터를 삭제하세요.
-- DELETE FROM employees where name = "민혁";

-- 8. 모든 직원을 position 별로 그룹화하여 각 직책의 평균 연봉을 계산하세요.
-- SELECT position, AVG(salary) AS salary_avg FROM employees GROUP BY position;

-- 9. employees 테이블을 삭제하세요.
-- DROP TABLE employees;