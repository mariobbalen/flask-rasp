from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from models import User, user_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = user_db.get(email)
        
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('main_dashboard'))
        
        flash('Email ou senha incorretos.')
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email in user_db:
            flash('Email ja cadastrado')
        else:
            User.create_user(email, password)
            return redirect(url_for('auth.login'))
        
        return render_template('registro.html   ')