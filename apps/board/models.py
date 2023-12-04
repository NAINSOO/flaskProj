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