from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

"""
(1) 블루프린트 :
    1-1) 모듈화: 어플레케이션의 서로 다른 부분을 모듈로 나누어 관리 가능
    1-2) 라우팅 관리: 라우트 별로 기능을 묶을 수 있다
    1-3) 뷰함수, 라우팅, 템플릿, 에러핸들링 등을 그룹화 가능 
    
(2) abort :
    클라이언트의 요청 처리 중에 오류가 발생했을 때 HTTP 상태코드와 함께 오류 메세지를 전송하는 함
    abort(404, message="Resource not found")

(3) 뷰(View): 사용자가 볼 수 있는 화면이나 인터페이스를 제공하는 컴포넌트.
    뷰 함수(View function): Flask에서 특정 라우트에 대한 요청을 처리하고 응답을 반환하는 함수.
    클래스 기반 뷰(Class-based view): 여러 HTTP 메서드를 처리하는 클래스를 정의하여 복잡한 로직을 구조화된 방식으로 관리하는 방법.
(4) MethondView: 클래스 기반 뷰를 사용하게 해주는 모듈
"""

book_blp = Blueprint('books', 'books', url_prefix='/books', description='Book route!!')

books = []


@book_blp.route('/')
class BookList(MethodView):
    @book_blp.response(200, BookSchema(many=True))  # 많은 값을 보여줄 수 있도록 설정
    def get(self):
        return books

    @book_blp.arguments(BookSchema) # blueprint로 데이터를 받았을 때 BookSchema를 이용해 유효성 검증
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
        new_data['id'] = len(books) + 1
        books.append(new_data)
        return new_data


@book_blp.route('/<int:book_id>')
class Book(MethodView):
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        return book

    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        book.update(new_data)
        return book

    @book_blp.response(204)
    def delete(self, book_id):
        global books
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        books = [book for book in books if book['id'] != book_id]
        return ''
