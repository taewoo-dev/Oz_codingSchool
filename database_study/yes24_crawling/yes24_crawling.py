from database.yes24_db import excute_query

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymysql
import pymysql.cursors

import re
import time
from datetime import datetime


def is_number(string):
    try:
        float(string)
        return False
    except ValueError:
        return True


ChromeDriverManager().install()
browser = webdriver.Chrome()

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="--------",
    database="yes24",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor  # json 형식으로 데이터가 전달되는 경우가 많다
)

link_list = []

for i in range(1, 4):
    print(f"현재 {i}page 수집 중")
    url = f"https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber={i}&pageSize=24"
    browser.get(url)
    title_list = browser.find_elements(By.CLASS_NAME, "gd_name")
    for data in title_list:
        link = data.get_attribute("href")
        link_list.append(link)
    time.sleep(7)

print(f"크롤링 리스트 갯수 : {len(link_list)}")

for link in link_list:
    browser.get(link)
    title = browser.find_element(By.CLASS_NAME, "gd_name").text
    author = browser.find_element(By.CLASS_NAME, "gd_auth").text
    publisher = browser.find_element(By.CLASS_NAME, "gd_pub").text

    publishing = browser.find_element(By.CLASS_NAME, "gd_date").text

    match = re.search(r'(\d+)년 (\d+)월 (\d+)일', publishing)

    if match:
        year, month, day = match.groups()
        data_obj = datetime(int(year), int(month), int(day))
        publishing = data_obj.strftime("%Y-%m-%d")
    else:
        publishing = "2024-01-01"
    try:
        rating = browser.find_element(By.CLASS_NAME, "yes_b").text
        if is_number(rating):
            rating = 0
    except:
        rating = 0
    try:
        reviews = browser.find_element(By.CLASS_NAME, "txC_blue").text
        reviews = int(reviews.replace(",", ""))
    except:
        reviews = 0

    sales = browser.find_element(By.CLASS_NAME, "gd_sellNum").text.split(" ")[2]
    sales = int(sales.replace(",", ""))

    price = browser.find_element(By.CLASS_NAME, "yes_m").text[:-1]
    price = int(price.replace(",", ""))

    full_text = browser.find_element(By.CLASS_NAME, "gd_best").text
    parts = full_text.split(" | ")
    ranking_part = parts[0]
    ranking = ''.join(filter(str.isdigit, ranking_part))

    try:
        full_text = browser.find_element(By.CLASS_NAME, "gd_best").text
        parts = full_text.split(" | ")
        ranking_weeks_part = parts[1]
        ranking_weeks = ''.join(filter(str.isdigit, ranking_weeks_part.split()[-1]))
    except:
        ranking_weeks = 0

    sql = """
    INSERT INTO Books (
        title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks
        )
    VALUES (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
    )
    """
    excute_query(conn, sql, title, author, publisher, publishing, rating, reviews, sales, price, ranking, ranking_weeks)
    ""
