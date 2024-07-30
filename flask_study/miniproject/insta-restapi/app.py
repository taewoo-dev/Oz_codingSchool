from flask import Flask, request, jsonify

users = [
    {
        "username": "leo",
        "posts": [{"title": "Town House", "likes": 120}]
    },
    {
        "username": "alex",
        "posts": [{"title": "Mountain Climbing", "likes": 350}, {"title": "River Rafting", "likes": 200}]
    },
    {
        "username": "kim",
        "posts": [{"title": "Delicious Ramen", "likes": 230}]
    }
]

app = Flask(__name__)


@app.route("/users", methods=["GET", "POST"])
def manage_users():
    # post request
    if request.method == 'POST':
        request_data = request.get_json()
        new_user = {
            "username": request_data["username"],
            "posts": [{
                "title": "first post",
                "likes": 0
            }]
        }
        users.append(new_user)
        return jsonify(new_user), 201
    # get request
    return jsonify({"users": users})


@app.route("/users/post/<string:username>", methods=["GET", "POST"])
def manage_posts(username):
    # post request
    if request.method == "POST":
        request_data = request.get_json()
        for user in users:
            if user["username"] == username:
                new_post = {
                    "title": request_data["title"],
                    "likes": request_data["likes"]
                }
                user["posts"].append(new_post)
                return jsonify(new_post)
        return {"message": "User not found"}, 404

    # get request
    for user in users:
        if user["username"] == username:
            return {"posts": user["posts"]}
    return {"message": "User not found"}, 404


@app.route("/users/post/like/<string:username>/<string:title>", methods=["PUT"])
def like_post(username, title):
    for user in users:
        if user["username"] == username:
            for post in user["posts"]:
                if post["title"] == title:
                    post["likes"] += 1
                    return jsonify(post)
    return {"message": "Post not found"}, 404


@app.route("/users/<string:username>", methods=["DELETE"])
def delete_user(username):
    global users
    users = [user for user in users if user["username"] != username]
    return {"message": "User deleted"}, 200


if __name__ == '__main__':
    app.run(debug=True)
