from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():  # put application's code here
    users = [
        {"username": "traveler", "name": "Alex"},
        {"username": "photographer", "name": "Sam"},
        {"username": "gourmet", "name": "Chris"}
    ]
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
