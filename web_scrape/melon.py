import bs4
import requests
from bs4 import BeautifulSoup

from models import Sing

header_user = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

"""
멜론 사이트 top 100 추출
[순위]
제목 : 정보
가수 : 정보
앨범 : 정보
"""

rank_50 = soup.find_all("tr", class_="lst50")
rank_100 = soup.find_all("tr", class_="lst100")

sing_list = []


def scrape(element: bs4.element.Tag):
    rank = element.find("span", class_="rank").text
    title = element.find("div", class_="ellipsis rank01").text.strip()
    singer = element.find("div", class_="ellipsis rank02").find("a").text
    album = element.find("div", class_="ellipsis rank03").text.strip()
    sing_list.append(Sing(rank, title, singer, album))


for sing in rank_50:
    scrape(sing)

for sing in rank_100:
    scrape(sing)


def print_sing():
    global sing
    for sing in sing_list:
        print(sing)


print_sing()
