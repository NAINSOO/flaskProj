from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class SignUpForm(FlaskForm):
    username = StringField(
        "사용자명",
        validators=[
            DataRequired(message="사용자명은 필수입니다."),
            Length(1, 30, message="30문자 이내로 입력해 주세요."),
        ],
    )

    email = StringField(
        "메일 주소",
        validators=[
            DataRequired(message="메일 주소는 필수입니다."),
            Email("메일 주소의 형식으로 입력해 주세요."),
        ],
    )

    password = PasswordField(
        "비밀번호",
        validators=[DataRequired(message="비밀번호는 필수입니다."), EqualTo('password_valid', '비밀번호가 일치하지 않습니다')]
    )

    password_valid = PasswordField(
        "비밀번호확인",
        validators=[DataRequired(message="비밀번호는 필수입니다.")]
    )

    submit = SubmitField("신규 등록")

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])