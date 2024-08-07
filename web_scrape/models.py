class Sing:
    def __init__(self, rank, title, singer, album):
        self.rank = rank
        self.title = title
        self.singer = singer
        self.album = album

    def __str__(self):
        return f" 음악 순위 : {self.rank}위 \n 제목 : {self.title} \n 가수 : {self.singer} \n 앨범 : {self.album} \n"


class Blog:
    def __init__(self, keyword, title, author):
        self.keyword = keyword
        self.title = title
        self.author = author

    def __str__(self):
        return f" 검색 키워드 : {self.keyword} \n 블로그 제목 : {self.title} \n 블로그 작성자 : {self.author} \n"


class Movie:
    def __init__(self, rank, title, reservation_rate, release_date):
        self.rank = rank
        self.title = title
        self.reservation_rate = reservation_rate
        self.release_date = release_date

    def __str__(self):
        return f" 영화 순위 : {self.rank} \n 영화 제목 : {self.title} \n 영화 예매율 : {self.reservation_rate} \n 영화 개봉일 {self.release_date} \n"
