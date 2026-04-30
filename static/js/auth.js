// URL base de tu API
const API_URL = "http://127.0.0.1:5000/api";

// ================= LOGIN =================
function login(e) {
    e.preventDefault();

    const username = document.getElementById('login_email').value;
    const password = document.getElementById('login_password').value;

    fetch(`${API_URL}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.message) {
            localStorage.setItem("user", username);
            alert("Login exitoso");
            window.location.href = "dashboard.html";
        } else {
            alert(data.error);
        }
    })
    .catch(err => console.error("Error:", err));
}


// ================= REGISTER =================
function register(e) {
    e.preventDefault();

    const username = document.getElementById('reg_usuario').value;
    const email = document.getElementById('reg_email').value;
    const password = document.getElementById('reg_password').value;

    fetch(`${API_URL}/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, email, password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.message) {
            alert("Registro exitoso");
        } else {
            alert(data.error);
        }
    })
    .catch(err => console.error("Error:", err));
}


// ================= SESIÓN (DASHBOARD) =================
document.addEventListener("DOMContentLoaded", () => {
    const user = localStorage.getItem("user");

    // Solo aplica si existe el elemento (dashboard)
    const usuarioElemento = document.getElementById("usuario");

    if (usuarioElemento) {
        if (!user) {
            window.location.href = "index.html";
        } else {
            usuarioElemento.innerText = "Usuario: " + user;
        }
    }
});


// ================= LOGOUT =================
function logout() {
    localStorage.removeItem("user");
    window.location.href = "index.html";
}