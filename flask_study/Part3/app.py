from flask import Flask, render_template
from flask_smorest import Api
from database.db import db
from dotenv import load_dotenv
import os

from models.user import User
from models.board import Board
from routes.users import user_blp
from routes.boards import board_blp
app = Flask(__name__)

load_dotenv()  # .env 파일 로드

# (1) flask app과 데이터베이스 연동
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
# (2) 데이터베이스를 ORM으로 이용할 수 있도록 설정
db.init_app(app)

# (3). 라우팅을 위한 blueprint 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# (4). API 등록
api = Api(app)


api.register_blueprint(user_blp)
api.register_blueprint(board_blp)

# (5). route마다 뷰함수 설정
@app.route("/manage-boards")
def manage_boards():
    return render_template("boards.html")


@app.route("/manage-users")
def manage_users():
    return render_template("users.html")


if __name__ == "__main__":
    with app.app_context():
        print("flask앱을 실행합니다")
        # models 폴더에 만든 데이터베이스 스키마를 통하여 테이블 생성
        db.create_all() # 데이터베이스의 테이블이 비어있을 경우에만 유효!!, 그렇지 않은 경우에는 마이그레이션을 통해 변경사항을 업데이트해야함
    app.run(debug=True)
