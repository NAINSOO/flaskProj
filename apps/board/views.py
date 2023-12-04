from flask import Blueprint, render_template, redirect, url_for
from apps.board.models import Board
from apps.board.forms import BoardForm

board = Blueprint("board",
                 __name__,
                 template_folder="templates",
                 static_folder="static",
                 )

@board.route("/")
def index():
    board_list = Board.query.order_by(Board.create_date.desc()).all()
    print(board_list)
    return render_template("board/index.html", board_list=board_list)


@board.route("/new", methods=["get","post"])
def create_board():
    form = BoardForm()
    if form.validate_on_submit():
        return redirect(url_for('board.index'))

    return render_template("board/create.html",form=form)