# 📌 PFO2 - Sistema de Gestión de Tareas (API Flask + SQLite)

Práctica Formativa Obligatoria 2 – Programación sobre Redes  
Autor: **Adrián Agata**  
Tecnicatura Superior en Desarrollo de Software  

---

## 🎯 Objetivo del proyecto

Desarrollar una API REST utilizando **Flask** y **SQLite**, que permita registrar usuarios, iniciar sesión y mostrar una página HTML con los usuarios registrados y sus hashes de contraseña. Todo con persistencia en base de datos y autenticación básica.

---

## 🧱 Tecnologías utilizadas

- Python 3
- Flask
- SQLite
- Werkzeug (hash de contraseñas)
- HTML (con render Jinja2)
- Postman (para pruebas)
- GitHub (para documentación)

---

## 📁 Estructura del proyecto

PFO2_Redes_AdriánAgata/<br>
├── servidor.py<br>
├── tareas.db<br>
├── templates/<br>
│ └── bienvenida.html<br>
├── img/<br>
│ ├── registro.png<br>
│ ├── login.png<br>
│ └── tareas.png<br>
├── README.md<br>
└── requirements.txt<br>


---

## ⚙️ Cómo ejecutar el proyecto

1. Clonar el repositorio:
```bash
git init
git clone https://github.com/adrianagata011/PFO2_Redes_AdrianAgata.git
cd PFO2_Redes_AdrianAgata
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate.bat
```
3. Instalá Flask:
```bash
pip install -r requirements.txt
```

4. Ejecutá el servidor:
```bash
python servidor.py
```

5. Usá Postman o navegador para probar los endpoints.

---

## 🔗 Endpoints disponibles

POST /registro
Registra un nuevo usuario.

Body (JSON):

```bash
{
  "usuario": "nombre",
  "contraseña": "1234"
}
```

POST /login
Verifica las credenciales del usuario.

Body (JSON):

```bash
{
  "usuario": "nombre",
  "contraseña": "1234"
}
```

GET /tareas
Devuelve una página HTML que muestra los usuarios registrados y sus hashes de contraseña.

---

## 🧪 Capturas de pantalla

- Registro de usuario:  
  ![Registro](img/registro.png)

- Inicio de sesión:  
  ![Login](img/login.png)

- Página HTML de bienvenida:  
  ![Tareas](img/tareas.png)

---

##❓ Respuestas conceptuales

¿Por qué hashear contraseñas?
Porque guardar contraseñas en texto plano es una mala práctica de seguridad. Si la base de datos es comprometida, los atacantes tendrían acceso directo a las credenciales. El hashing transforma la contraseña en una cadena irreversible, haciendo que incluso si se filtra, no sea utilizable. Además, los hashes usan salts (semillas) que dificultan ataques de diccionario o rainbow tables.

¿Por qué usar SQLite para este proyecto?
SQLite es una base de datos liviana, de tipo embebido, que no requiere instalación ni configuración de servidor. Ideal para proyectos pequeños o educativos, permite almacenar datos persistentes en un solo archivo. Es portable, simple de usar y cumple con todos los requisitos para esta práctica.

---

## ✅ Estado del proyecto
✔ Registro funcionando
✔ Login funcionando
✔ Página HTML dinámica mostrando usuarios y hashes
✔ Pruebas realizadas con curl y Postman
✔ Documentación completa

---

## 🚀 Publicación
El proyecto fue subido a GitHub y puede ser consultado desde:
🔗 [URL de tu repositorio] (completalo cuando lo subas)

---