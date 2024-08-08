from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from models import Sing

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, '.img-logo').click()
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, '.nav_item:nth-of-type(3) > a').click()
time.sleep(0.5)

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
time.sleep(0.5)

driver.find_element(By.XPATH, "//button[@onclick='hasMore2();']").click()
time.sleep(0.5)

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
time.sleep(0.5)

soup = BeautifulSoup(driver.page_source, "html.parser")

sings = soup.find("ul",id='_chartList').find_all("li", class_="list_item")
print(len(sings))

sing_list = []


for sing in sings:
    title = sing.find("p", class_="title").text.strip()
    singer = sing.find("span", class_="name").text.strip()
    rank = sing.find("div", class_="ranking_num").text.strip()[:-1]

    sing_list.append(Sing(rank,title,singer,album=""))

for sing in sing_list:
    print(sing)

driver.quit()
