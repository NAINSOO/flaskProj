from apps.app import db
from apps.auth.models import User

class Board(db.Model):
    __tablename__ = "board"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('userinfo.id', ondelete='CASCADE'), nullable=True, server_default='1')
    user = db.relationship('User', backref=db.backref('board_set'))

class Answer(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('userinfo.id', ondelete='CASCADE'), nullable=True, server_default='1')
    user = db.relationship('User', backref=db.backref('answer_set'))
    board_id = db.Column(db.Integer, db.ForeignKey('board.id', ondelete='CASCADE'), nullable=True, server_default='1')
    board = db.relationship('Board', backref=db.backref('answer_set'))
