from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api/v1/feeds", methods=['GET'])
def show_all_feeds():
    return {
        'result': "success",
        'data': {
            "feed1": "data",
            "feed2": "data2"
        }
    }


# URL을 통해 데이터를 받는 경우 그 데이터를 함수에 사용
@app.route("/api/v1/feeds/<int:feed_id>", methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    return jsonify({
        'result': 'success',
        'data': {
            feed_id: "data"
        }
    })


@app.route("/api/v1/feeds", methods=['POST'])
def create_one_feed():
    # request는 클라이언트 측에서 보낸 데이터를 의미 form 형식의 request
    name = request.form['name']
    age = request.form['age']
    print(name, age)
    return jsonify({'result': 'success'})


datas = [{
    "name": "item1",
    "price": 10
}]


@app.get("/datas")
def get_datas():
    return {
        'datas': datas
    }  # (1). dict 형식은 Json형식으로 자동 형변환


@app.post("/datas")
def create_data():
    # request는 클라이언트 측에서 보낸 데이터를 의미 Json 형식의 request
    request_data = request.get_json()  # 요청 데이터를 Json 형식으로 변환

    print(request_data)

    new_data = {
        "items": request_data.get("items", [])
    }
    datas.append(new_data)
    for i in datas:
        print(i)
    return "post 성공", 201
