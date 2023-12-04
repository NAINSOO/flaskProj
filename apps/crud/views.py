from flask import Blueprint, render_template
from apps.app import db
from apps.auth.models import User
from apps.crud.forms import UserForm
from flask import redirect, url_for, flash
from sqlalchemy import exc

crud = Blueprint("crud",
                 __name__,
                 template_folder="templates",
                 static_folder="static",
                 )

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

@crud.route("/users/<user_id>",methods=["GET","POST"])
def edit_user(user_id):
    form = UserForm()

    user = User.query.filter_by(id=user_id).first()

    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        try:
            db.session.add(user)
            db.session.commit()
        except exc.IntegrityError as error:
            if error.orig.args[0] == 1062:
                flash("중복된 이메일 주소입니다.")
                return redirect(url_for("crud.edit_user", user_id=user_id))
            else:
                flash('MySQL error: {}'.format(error))
                return redirect(url_for("crud.edit_user", user_id=user_id))
        return redirect(url_for("crud.users"))
    return render_template("crud/edit.html",form=form, user=user)


@crud.route('/users/<user_id>/delete', methods=['post'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))