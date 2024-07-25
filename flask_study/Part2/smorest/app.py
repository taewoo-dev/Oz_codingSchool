from flask import Flask
from flask_smorest import Api
from api import blp

# (1) blueprint: route 별로 기능을 묶는 클래스
# (2) abort: 오류에 대한 응답 처리 클래스
# (3) schema: 데이터의 유효성 검증을 위한 클래
app = Flask(__name__)

# OpenAPI 관련 설정 restapi를 이쁘게 보여주는 툴 -> 스웨거 이용
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True)
