from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class BoardForm(FlaskForm):
    title = StringField(
        "제목",
        validators=[
            DataRequired(message="제목은 필수입니다."),
            Length(1, 30, message="30문자 이내로 입력해 주세요."),
        ],
    )

    content = StringField(
        "내용",
        validators=[
            DataRequired(message="내용은 필수입니다."),
            Length(1, 500, message="500문자 이내로 입력해 주세요."),
        ],
    )

    submit = SubmitField("신규 등록")