import requests
from bs4 import BeautifulSoup

from models import Movie

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

movie_list = []

charts = soup.find("div", class_="sect-movie-chart").find_all("ol")


for chart in charts:
    movies = chart.find_all("li")
    for movie in movies:
        rank = movie.find("strong", class_="rank").text
        title = movie.find("strong", class_="title").text
        reservation_rate = movie.find("strong", class_="percent").find("span").text
        release_date = movie.find("span", class_="txt-info").text.split()[0]
        movie_list.append(Movie(rank,title,reservation_rate,release_date))

for movie in movie_list:
    print(movie)
