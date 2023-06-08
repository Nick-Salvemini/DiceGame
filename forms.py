from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Optional, Email


class RegisterForm(FlaskForm):
    '''Form to register'''

    email = StringField('Email', validators=[InputRequired(), Email()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[InputRequired()])


class LoginForm(FlaskForm):
    '''Form to Login'''

    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
