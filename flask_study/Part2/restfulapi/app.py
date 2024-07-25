from flask import Flask
from flask_restful import Api
from resources.item import Item

app = Flask(__name__)

# (1). 다른 라이브러리를 사용하기 위해서 initializing
api = Api(app)

# 경로 추가
api.add_resource(Item, '/item/<string:name>')