# 🔐 Sistema de Login y Registro con Flask + SQL Server

Aplicación web completa que implementa un sistema de autenticación (login y registro) utilizando:

- 🐍 Python (Flask)
- 🗄 SQL Server (pyodbc)
- 🌐 HTML, CSS y JavaScript
- 🔗 API REST
- 💾 LocalStorage para manejo de sesión (frontend)

---

## 🚀 Características

- ✔ Registro de usuarios
- ✔ Inicio de sesión
- ✔ Conexión a base de datos SQL Server
- ✔ API REST con Flask
- ✔ Validación básica de datos
- ✔ Manejo de errores
- ✔ Dashboard protegido
- ✔ Separación de frontend y backend
- ✔ Uso de entorno virtual (.venv)

---

## 🧠 Tecnologías utilizadas

- Python 3
- Flask
- Flask-CORS
- pyodbc
- SQL Server Express
- HTML5
- CSS3
- JavaScript (Fetch API)

---

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/login_register.git
cd login_register
```

---

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

Activar entorno:

```bash
.\.venv\Scripts\activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Configurar base de datos

1. Abrir SQL Server Management Studio  
2. Ejecutar el archivo:

```sql
database.sql
```

Esto creará:
- Base de datos `login_registro`
- Tabla `usuarios`

---

### 5. Ejecutar la aplicación

```bash
python app.py
```

Abrir en el navegador:

```
http://127.0.0.1:5000/
```

---

## 🔗 Endpoints API

### 📝 Registro

```
POST /api/register
```

Body JSON:

```json
{
  "username": "usuario",
  "email": "correo@gmail.com",
  "password": "123456"
}
```

---

### 🔐 Login

```
POST /api/login
```

Body JSON:

```json
{
  "username": "usuario",
  "password": "123456"
}
```

---

## 🔒 Seguridad (Actual)

⚠️ Nota:

- Las contraseñas actualmente se almacenan en texto plano (solo para fines educativos)



## 🧑‍💻 Autor

**Chuaz Gómez**  
📍 México  
📧 Chuazgomez3@gmail.com  
🔗 GitHub: https://github.com/chuazgomez3-design  

---

## 💬 Frase del proyecto

> “El frontend muestra… el backend procesa… y la base de datos guarda la verdad.”
<img width="1427" height="556" alt="servidor" src="https://github.com/user-attachments/assets/4dc2d3a3-d505-44ca-afcf-cc1894fa977b" />
<img width="1901" height="968" alt="registro_usuario" src="https://github.com/user-attachments/assets/5e6bf58c-4576-40eb-8162-1d7e9ff66b78" />
<img width="1910" height="961" alt="iniciar_sesion" src="https://github.com/user-attachments/assets/c9cbbaf9-eb0d-4af3-81bc-c4a933b9e460" />
