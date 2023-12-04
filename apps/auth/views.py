from flask import Blueprint,render_template, flash, redirect, url_for, session, request, g
from apps.auth.forms import SignUpForm, UserLoginForm
from apps.auth.models import User
from apps.app import db
from sqlalchemy import exc
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth",
                 __name__,
                 template_folder="templates",
                 static_folder="static",
                 )

@auth.route("/")
def index():
    return render_template("auth/index.html")

@auth.route("/signup", methods=['get','post'])
def signup():
    form = SignUpForm()
    
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        try:
            db.session.add(user)
            db.session.commit()
        except exc.IntegrityError as error:
            if error.orig.args[0] == 1062:
                flash("중복된 이메일 주소입니다.")
                return redirect(url_for("auth.signup"))
            else:
                flash('MySQL error: {}'.format(error))
                return redirect(url_for("auth.signup"))
        return redirect(url_for("crud.users"))
    return render_template('auth/signup.html',form=form)

@auth.route('/login', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password_hash, form.password.data):
            print(user.password_hash,"  ",generate_password_hash(form.password.data))
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('crud.users'))
        flash(error)
    return render_template('auth/login.html', form=form)

@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('crud.users'))