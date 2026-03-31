from flask import Flask, request, jsonify, render_template, Blueprint, redirect, url_for
from models.context import *
from models.user import *
from flask_login import LoginManager, login_required, current_user, login_user

main_routes = Blueprint("main", __name__)

@main_routes.route('/user', methods=['POST', 'GET'])
def use_api():
    try:
        if request.method == "POST":
            value = request.json.get('data')  # Recebe o valor do corpo da requisição JSON
        
            if value is None:
                return jsonify({"error": "No value provided"}), 400
        
            insert_data(value)
            
            return jsonify({"message": "Value added successfully"}), 201
        
        elif request.method == "GET":
            
            rows = select_data()

            values = [{"id": row[0], "data": row[1]} for row in rows]

            return jsonify(values), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@main_routes.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form.get('username') == 'admin' and request.form.get('password') == 'admin':
            login_user(user('admin'))
            return redirect(url_for('main.home'))
        else:
            error = 'Invalid credentials.'

    return render_template('login.html', error=error)

@login_required
@main_routes.route("/home", methods=['GET'])
def home():
    return render_template("home.html")