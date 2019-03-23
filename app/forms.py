from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SubmitField, PasswordField, StringField, BooleanField


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')