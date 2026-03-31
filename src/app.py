# Criado por Fernando Pozzer 2025
# Alterado port Rafael Reis 2026
from flask import Flask, request, jsonify
from models.context import *
from routes.main_routes import main_routes

app = Flask(__name__, template_folder="views")
app.register_blueprint(main_routes)

if __name__ == '__main__':
    create_table()
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000, debug=True)