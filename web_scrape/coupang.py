from bs4 import BeautifulSoup
import requests

keyword = input("검색 내용").strip()

url = f"https://www.coupang.com/np/search?component=&q={keyword}"

header_user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

"""
쿠팡에는 쿠키정보를 추가해서 보내야함
"""

cookie = {
    "cookie": "apple"
}

req = requests.get(url, headers=header_user, cookies=cookie, timeout=3)

html = req.text

soup = BeautifulSoup(html, "html.parser")

# container = soup.find("div", class_="search-content").find("ul", class_="search-product-list")
#
# products = container.find_all("li", class_="search-product")

# items = soup.select(".search-product")

# 정확히 class=search-product  인 태그만 가져오기
items = soup.select("[class=search-product  ]")

for rank, item in enumerate(items,1):
    name = item.select_one(".name").text
    price = item.select_one(".price-value").text
    link = f"https://www.coupang.com/{item.a['href']}"
    img_src = item.select_one(".search-product-wrap-img")
    rocket = item.select_one(".badge.rocket")


    print(f"{rank}위")
    print(name)
    print(f"{price}원")
    print(f"쿠팡 링크 : {link}")
    if rocket:
        print("로켓 배송 가능")
    else:
        print("로켓 배송 불가능")
    if img_src.get("data-img-src"):
        img_url = f"http:{img_src.get('data-img-src')}"
    else:
        img_url = f"http:{img_src.get('src')}"
    print(f"이미지 링크 : {img_url}")
    print("\n")

    img_req = requests.get(img_url)

    with open(f"img/{rank}.png", "wb") as f:
        f.write(img_req.content)
