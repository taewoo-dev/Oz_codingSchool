from flask import request
from flask_restful import Resource

items = []


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {"msg": "Item not found"}, 404  # msg, code

    def post(self, name):
        for item in items:
            if item["name"] == name:
                return {"msg": "Item Already exists"}, 400
        data = request.get_json()
        item = {
            "name": name,
            "price": data['price']
        }
        items.append(item)
        return item, 201

    def put(self, name):
        data = request.get_json()
        for item in items:
            if item['name'] == name:
                item['name'] = data['price']
                return item
        # 아이템이 존재하지 않으면 새로운 아이템 추가
        new_item = {
            "name": name,
            "price": data['price']
        }
        items.append(new_item)
        return new_item

    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        return {"msg": "Item deleted"}
