from flask import Blueprint, render_template, redirect, url_for, session, g, flash, request
from apps.board.models import Board
from apps.board.forms import BoardForm
from apps.app import db
import datetime
from sqlalchemy import exc
board = Blueprint("board",
                 __name__,
                 template_folder="templates",
                 static_folder="static",
                 )

@board.route("/")
def index():
    board_list = Board.query.order_by(Board.create_date.desc()).all()
    return render_template("board/index.html", board_list=board_list)


@board.route("/new", methods=["get","post"])
def create_board():
    user = g.user

    if user == None:
        flash("로그인 상태가 아닙니다.")
        return redirect(url_for('auth.login'))
    form = BoardForm()
    if form.validate_on_submit():
        board = Board(title = form.title.data, content = form.content.data, user_id = user.id, create_date = datetime.datetime.now())
        try:
            db.session.add(board)
            db.session.commit()
        except exc.IntegrityError as error:
            flash('MySQL error: {}'.format(error))
            return redirect(url_for("board.create_board"))
        return redirect(url_for('board.index'))

    return render_template("board/create.html",form=form)


@board.route("/detail/<board_id>", methods=["get", "post"])
def detail_board(board_id):
    board = Board.query.filter_by(id=board_id).first()
    return render_template("board/detail.html",board = board)


@board.route("/edit/<board_id>", methods=['get', 'post'])
def edit_board(board_id):
    board = Board.query.filter_by(id=board_id).first()
    user = g.user

    if user == None:
        flash("로그인 상태가 아닙니다.")
        return redirect(url_for('auth.login'))
    elif board == None:
        flash("글이 존재하지 않습니다.")
        return redirect(url_for('board.index'))
    elif user.id != board.user_id:
        flash("글쓴이가 아닙니다.")
        return redirect(url_for('board.index'))
    
    form = BoardForm()
    if request.method == 'GET': 
        form.title.data = board.title
        form.content.data = board.content
    if form.validate_on_submit():
        board.title = form.title.data
        board.content = form.content.data
        try:
            db.session.add(board)
            db.session.commit()
        except exc.IntegrityError as error:
            flash('MySQL error: {}'.format(error))
            return redirect(url_for("board.edit_board"))
        return redirect(url_for('board.index'))

    return render_template('board/edit.html',form=form, board=board)

@board.route("delete/<board_id>", methods=['get'])
def delete_board(board_id):
    board = Board.query.filter_by(id=board_id).first()
    user = g.user

    if user == None:
        flash("로그인 상태가 아닙니다.")
        return redirect(url_for('auth.login'))
    elif board == None:
        flash("글이 존재하지 않습니다.")
        return redirect(url_for('board.index'))
    elif user.id != board.user_id:
        flash("글쓴이가 아닙니다.")
        return redirect(url_for('board.index'))
    try:
        db.session.delete(board)
        db.session.commit()
    except exc.IntegrityError as error:
        flash('MySQL error: {}'.format(error))
        return redirect(url_for("board.edit_board"))

    return redirect(url_for('board.index'))