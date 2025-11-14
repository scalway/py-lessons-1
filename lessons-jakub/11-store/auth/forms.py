from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zarejestruj')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj')