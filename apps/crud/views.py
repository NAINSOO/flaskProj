from flask import Blueprint, render_template
from apps.app import db
from apps.crud.models import User
from apps.crud.forms import UserForm
from flask import redirect, url_for, flash
from sqlalchemy import exc

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

@crud.route("/users/new", methods=["GET","POST"])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data,              
        )
        try:
            db.session.add(user)
            db.session.commit()
        except exc.IntegrityError as error:
            if error.orig.args[0] == 1062:
                flash("중복된 이메일 주소입니다.")
                return redirect(url_for("crud.create_user"))
            else:
                flash('MySQL error: {}'.format(error))
                return redirect(url_for("crud.create_user"))
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)

@crud.route("/users")
def users():
    users = User.query.all()
    return render_template("crud/index.html",users=users)