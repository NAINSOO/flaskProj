from flask import Blueprint, render_template
from apps.app import db
from apps.crud.models import User

crud = Blueprint("crud",
                 __name__,
                 template_folder="templates",
                 static_folder="static",
                 )

@crud.route("/")
def index():
    return render_template("crud/index.html")

@crud.route("/sql")
def sql():
    db.session.query(User).all()
    user = User(username="홍길동", email="flask@example.com", password="1234")   
    db.session.add(user)
    db.session.commit()

    return "콘솔 로그를 확인해 주세요"