import requests
from bs4 import BeautifulSoup
from models import Blog
header_user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어 : ")

url = base_url + keyword
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# 광고 배너의 id 또는 class 명을 찾아보세요
# 광고 배너의 결과값을 변수 담아서 if문으로 검증을 합니다.
# 아무것도 없는 경우는 어떤 값이 들어가는지 확인해주세요
# if문의 참과 거짓일 경우 어떻게 작동하는지에 대한 원리를 상기시켜보세요

blog_list = []
wrap = soup.select(".view_wrap")

for i in wrap:
    if not i.select_one(".spblog.ico_ad"):
        title = i.select(".title_link")
        author = i.select(".name")
        blog_list.append(Blog(keyword,title[0].text,author[0].text))

for i in blog_list:
    print(i)