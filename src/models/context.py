import sqlite3

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

def insert_data(value):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO data (value) VALUES (?)', (value,))
        conn.commit()

def select_data():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM data')
        return cursor.fetchall()