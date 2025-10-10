from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bs4 import Bootstrap
from flask_wtf  import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired
import secrets

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)

VALID_USERNAME = 'admin'
VALID_PASSWORD = '1234'

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.username.data == VALID_USERNAME and login_form.password.data == VALID_PASSWORD:
            session['user'] = login_form.username.data
            flash(message='Login Successful', category='success')
            return redirect(url_for('dashboard'))
        else:
            flash(message='Login Unsuccessful', category='danger')
    return render_template('login.html', title='Logowanie', login_form=login_form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashborad.html', title='Dashboard')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)