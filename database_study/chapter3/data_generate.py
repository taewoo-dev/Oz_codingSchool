import mysql.connector
from faker import Faker # 데이터 랜덤 생성 라이브러리
import random

# (1) MYSQL 설정
db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1520528a",
    database = "mydatabase"
)

# (2) MYSQL 연결
cursor = db_connection.cursor()
faker = Faker()

# (3) 100개의 user 더미 데이터 생성 
for _ in range(100):
    username = faker.user_name()
    email = faker.email()

    # 파라미터화된 쿼리 사용
    sql = "INSERT INTO users(username, email) VALUES (%s, %s)"
    values = (username, email)
    cursor.execute(sql, values)

cursor.execute("select user_id from users") # cursor 인스턴스에 가져온 데이터가 담겨있다
vaild_user_id = [row[0] for row in cursor.fetchall()]

# (4) 100개의 order 더미 데이터 생성
for _ in range(100):
    user_id = random.choice(vaild_user_id)
    product_name = faker.word()
    quantity = random.randint(1,10)

    try:
        sql = "INSERT INTO orders (user_id, product_name, quantity) VALUES(%s, %s, %s)"
        values = (user_id,product_name,quantity)
        cursor.execute(sql, values)
    except:
        print("전송 오류!!")
        pass
# 변경사항 커밋
db_connection.commit()

# 커서와 연결 종료
cursor.close()
db_connection.close()

