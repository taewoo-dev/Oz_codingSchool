from typing import Optional, Any, Union

import pymysql
import pymysql.cursors


def excute_query(conn, sql: str, *values: Optional[tuple]) -> Optional[list]:
    """
    parameter:
        conn: 연결한 데이터 베이스 객체
        sql: 원하는 쿼리
        values: 쿼리에 전달되는 변수
    """

    with conn.cursor() as cursor:
        cursor.execute(sql, values) # 쿼리 실행

        if sql.strip().upper().startswith("SELECT"): # select의 경우 결과가져와 보여준다
            return cursor.fetchall()
        else: # 나머지의 경우 변경사항을 커밋
            conn.commit()


def main():

    conn = pymysql.connect(
                            host="localhost",
                            user="root",
                            password="1520528a",
                            database="airbnb_db",
                            charset="utf8mb4",
                            cursorclass=pymysql.cursors.DictCursor # json 형식으로 데이터가 전달되는 경우가 많다
                            )

    try:
        # (1). Products tabel에 새로운 제품 추가
        sql = "insert into Products (productName, price, stockQuantity)\
            values (%s, %s, %s)"
        excute_query(conn, sql, "아이폰", 100, 10)

        # (2). Customers 고객 목록 조회
        sql = "select * from Customers"
        result = excute_query(conn, sql)
        for row in result:
            print(row)
    
        # (3). Products 제품 재고 업데이트 - 아이폰 재고 3개 판매
        sql = "update Products set stockQuantity = stockQuantity - %s where productName = %s"
        excute_query(conn, sql, 3, "아이폰")

        # (4). Orders 고객별 총 주문 계산
        sql = "select customerID, SUM(totalAmount) from Orders group by customerID"
        result = excute_query(conn, sql)
        for row in result:
            print(row)

        # (5). 고객 이메일 이벤트 / 고객 아이디를 입력받고, 새로운 이메일 주소로 업데이트
        sql = "update Customers set email = %s where customerID = %s"
        excute_query(conn, sql, "newid입니다", 5)

        # (6). Orders 원하는 주문 ID 삭제 주문취소 
        sql = "delete from Orders where orderID = %s"
        excute_query(conn, sql, 15)

        # (7). Products 테이블에서 제품 검색하는 쿼리
        sql = "select * from Products where productName = %s"
        result = excute_query(conn, sql, "아이폰")
        for row in result:
            print(row)

        # (8). 특정 고객의 모든 주문 조회
        sql = "select * from Orders where customerID = %s"
        result = excute_query(conn, sql, 4)
        for row in result:
            print(row)

        # (9). 가장 많은 주문을 한 고객 찾기
        # sql = "select customerID, COUNT(*) as max_orders from Orders group by customerID order by max_orders DESC limit 1"
        sql = "select c.customerName, o.max_orders from Customers as c\
                INNER JOIN (SELECT customerID, COUNT(*) as max_orders FROM Orders GROUP BY customerID ORDER BY max_orders DESC LIMIT 1) o ON o.customerID = c.customerID;"
        
        result = excute_query(conn, sql)

        for i in result:
            print(i)

    finally:
        conn.close()

if __name__ == "__main__":
    main()
    
    