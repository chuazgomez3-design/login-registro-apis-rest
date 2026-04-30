from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)

# HOME
@app.route('/')
def home():
    return render_template('index.html')


# CONEXIÓN
def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=tu-servidor_sqlserver;"
        "DATABASE=nombre_base_datos;"
        "Trusted_Connection=false;"
        "TrustServerCertificate=false;"
    )


# REGISTER
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    nombre_usuario = data.get('username')
    correo_usuario = data.get('email')
    password_usuario = data.get('password')

    if not nombre_usuario or not correo_usuario or not password_usuario:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuarios (nombre_usuario, correo_usuario, password_usuario)
            VALUES (?, ?, ?)
        """, (nombre_usuario, correo_usuario, password_usuario))

        conn.commit()

        return jsonify({"message": "Usuario registrado correctamente"}), 201

    except pyodbc.IntegrityError:
        return jsonify({"error": "El usuario o correo ya existe"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()


# LOGIN
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    usuario = data.get('username')
    password = data.get('password')

    if not usuario or not password:
        return jsonify({"error": "Datos incompletos"}), 400

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM usuarios 
            WHERE nombre_usuario = ? AND password_usuario = ?
        """, (usuario, password))

        user = cursor.fetchone()

        if user:
            return jsonify({"message": "Login exitoso"}), 200
        else:
            return jsonify({"error": "Credenciales incorrectas"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()


#  RUN
if __name__ == '__main__':
    app.run(debug=True)