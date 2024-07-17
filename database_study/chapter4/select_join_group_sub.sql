-- 기본 조회 및 필터링
-- select * from customers;
-- select * from products where productLine = "Classic Cars";
-- select * from orders order by orderDate desc limit 10;
-- select * from payments where amount >= 100;

-- 조인 쿼리
-- select orderNumber,customerName from orders
-- join customers on orders.customerNumber = customers.customerNumber;
-- select productName, textDescription from products
-- join productlines on products.productLine = productlines.productLine;

-- SELECT e1.employeeNumber, e1.firstName, e1.lastName, e2.firstName AS 'ManagerFirstName', e2.lastName AS 'ManagerLastName'
-- FROM employees e1
-- LEFT JOIN employees e2 ON e1.reportsTo = e2.employeeNumber;

-- select employees.employeeNumber, employees.lastName, employees.firstName from employees
-- join offices on employees.officeCode = offices.officeCode
-- where offices.city = "San Francisco";

-- 그룹 쿼리 
-- select productLine, COUNT(*) as productCount from products
-- group by productLine;

-- select customers.customerNumber,
-- 	   customers.customerName,
--        SUM(orderdetails.quantityOrdered * orderdetails.priceEach) as totalAmount
--        from customers
--        join orders on customers.customerNumber = orders.customerNumber
--        join orderdetails on orders.orderNumber = orderdetails.orderNumber
--        group by customers.customerNumber, customers.customerName;

-- select productName, SUM(quantityOrdered) as totalQuantity
-- from orderdetails od
-- join products p on od.productCode = p.productCode
-- group by productName
-- order by totalQuantity Desc
-- limit 10;

-- select o.city, SUM(od.quantityOrdered * od.priceEach) as totalSales
-- from orders ord
-- join orderdetails od on ord.orderNumber = od.orderNumber
-- join customers c on ord.customerNumber = c.customerNumber
-- join employees e on c.salesRepEmployeeNumber = e.employeeNumber
-- join offices o on e.officeCode = o.officeCode
-- group by o.city
-- order by totalSales Desc
-- limit 10;

-- 서브 쿼리 
-- WHERE는 그룹화되기 전에 각 행을 필터링, Having은 그룹화된 후 각 행을 필터
-- select orderNumber, sum(quantityOrdered * priceEach) as totalAmount
-- From orderdetails
-- group by orderNumber
-- having orderNumber > 500;

