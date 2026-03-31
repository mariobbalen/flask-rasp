# Criado por Fernando Pozzer 2025
# Alterado port Rafael Reis 2026
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
# Função para conectar ao banco de dados SQLite
def connect_db():
    return sqlite3.connect('data.db')

# Função para criar a tabela se não existir
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value TEXT NOT NULL
        )"""
    )
    conn.commit()
    conn.close()

# Inicializa a tabela ao iniciar o aplicativo
create_table()

@app.route('/', methods=['POST', 'GET'])
def use_api():
    try:
        if request.method == "POST":
            value = request.json.get('data')  # Recebe o valor do corpo da requisição JSON
        
            if value is None:
                return jsonify({"error": "No value provided"}), 400
        
            with connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO data (value) VALUES (?)', (value,))
                conn.commit()
            
            return jsonify({"message": "Value added successfully"}), 201
        
        elif request.method == "GET":
            with connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM data')
                rows = cursor.fetchall()

            values = [{"id": row[0], "data": row[1]} for row in rows]

            return jsonify(values), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
