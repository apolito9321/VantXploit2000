import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Creamos la tabla (igual que el modelo User del tutorial)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Función para registrar usuario (como signup_post del tutorial)
def register_user(email, name, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Verificamos si ya existe (igual que en el tutorial)
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    if cursor.fetchone():
        conn.close()
        return False  # Ya existe
    
    hashed_password = generate_password_hash(password)  # Hash seguro
    cursor.execute("INSERT INTO users (email, name, password) VALUES (?, ?, ?)", 
                   (email, name, hashed_password))
    conn.commit()
    conn.close()
    return True

# Función para verificar login (igual que login_post del tutorial)
def verify_login(email, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    
    if user and check_password_hash(user[0], password):
        return True
    return False

# Inicializamos la DB al importar
init_db()