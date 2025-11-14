from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required

from .forms import LoginForm, RegisterForm
from extensions import db, bcrypt
from models import Users

auth_bp = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = Users.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            flash('Zalogowano poprawnie', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Nieprawidłowy login lub hasło', 'danger')
    return render_template('auth/login.html', title='Logowanie', login_form=login_form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    register_form = RegisterForm()
    if register_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
        new_user = Users(email=register_form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Konto utworzone poprawnie', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Rejestracja', register_form=register_form)

@auth_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Wylogowano poprawnie', 'success')
    return redirect(url_for('auth.login'))

@auth_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('auth/dashboard.html', title='Dashboard')