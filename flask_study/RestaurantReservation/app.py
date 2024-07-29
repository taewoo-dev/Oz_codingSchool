from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from datetime import datetime
app = Flask(__name__)

load_dotenv()  # .env 파일 로드

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255), nullable=False)
    customer_phone = db.Column(db.String(255), nullable=False)
    reservation_time = db.Column(db.DateTime, nullable=False)
    number_of_people = db.Column(db.Integer, nullable=False)
    special_requests = db.Column(db.Text)

    def __repr__(self):
        return f"<Reservation {self.customer_name}>"


def create_tables():
    db.create_all()


# Home route to show reservations and a form to add new ones
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_reservation = Reservation(
            customer_name=request.form['customer_name'],
            customer_phone=request.form['customer_phone'],
            reservation_time=request.form['reservation_time'],
            number_of_people=request.form['number_of_people'],
            special_requests=request.form['special_requests']
        )
        db.session.add(new_reservation)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        all_reservations = Reservation.query.all()
        return render_template('index.html', reservations=all_reservations)


if __name__ == '__main__':
    with app.app_context():
        print("flask앱을 실행합니다")
        create_tables()  # 데이터베이스의 테이블이 비어있을 경우에만 유효!!, 그렇지 않은 경우에는 마이그레이션을 통해 변경사항을 업데이트해야함
    app.run(debug=True)
