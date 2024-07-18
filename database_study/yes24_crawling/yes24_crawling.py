from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ChromeDriverManager().install()
browser = webdriver.Chrome()

link_list = []
for i in range(1, 4):
    print(f"현재 {i}page 수집 중")
    url = f"https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber={i}&pageSize=24"
    browser.get(url)
    title_list = browser.find_elements(By.CLASS_NAME, "gd_name")
    for data in title_list:
        link = data.get_attribute("href")
        link_list.append(link)
    time.sleep(3)

print(f"크롤링 리스트 갯수 : {len(link_list)}")

for link in link_list:
    browser.get(link)
    title = browser.find_element(By.CLASS_NAME,"gd_name").text
    author = browser.find_element(By.CLASS_NAME, "gd_auth").text
    publisher = browser.find_element(By.CLASS_NAME, "gd_pub").text
    publishing = browser.find_element(By.CLASS_NAME, "gd_date").text
    rating = browser.find_element(By.CLASS_NAME, "yes_b").text
    reviews = browser.find_element(By.CLASS_NAME, "txC_blue").text
    sales = browser.find_element(By.CLASS_NAME, "gd_sellNum").text.split(" ")[2]
    price = browser.find_element(By.CLASS_NAME, "yes_m").text[:-1]
    ranking = browser.find_element(By.CLASS_NAME, "gd_best").text.split(" | ")[0]
    ranking_weeks = browser.find_element(By.CLASS_NAME, "gd_best").text.split(" | ")[1]
