from flask import Flask, request, jsonify, render_template
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Crear tabla si no existe
def crear_tabla():
    with sqlite3.connect("usuarios.db") as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                contraseña TEXT NOT NULL
            );
        ''')
crear_tabla()

@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    usuario = data.get("usuario")
    contraseña = generate_password_hash(data.get("contraseña"))

    try:
        with sqlite3.connect("tareas.db") as conn:
            conn.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", (usuario, contraseña))
        return jsonify({"mensaje": "Usuario registrado con éxito"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Usuario ya existe"}), 409

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get("usuario")
    contraseña = data.get("contraseña")

    with sqlite3.connect("tareas.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT contraseña FROM usuarios WHERE usuario = ?", (usuario,))
        row = cur.fetchone()
        if row and check_password_hash(row[0], contraseña):
            return jsonify({"mensaje": "Login exitoso"}), 200
        else:
            return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route('/tareas', methods=['GET'])
def tareas():
    with sqlite3.connect("tareas.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT usuario, contraseña FROM usuarios")
        usuarios = [{"nombre": row[0], "hash": row[1]} for row in cur.fetchall()]
    return render_template("bienvenida.html", usuarios=usuarios)



if __name__ == '__main__':
    app.run(debug=True)
