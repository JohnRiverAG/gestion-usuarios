# 🧑‍💼 Gestión de Usuarios

Aplicación web desarrollada con Django para la gestión de usuarios. Permite registrar, editar, eliminar y autenticar usuarios a través de una interfaz sencilla y funcional.

---

## 🚀 Características

- Registro de nuevos usuarios
- Inicio de sesión y cierre de sesión
- Panel de control con lista de usuarios
- Edición y eliminación de usuarios
- Validación de formularios
- Plantillas HTML personalizadas
- Sistema de autenticación integrado con Django

---

## 🛠️ Tecnologías

- **Python 3.13+**
- **Django**
- **SQLite** (por defecto, fácilmente adaptable a PostgreSQL o MySQL)
- HTML5 + CSS3 (para las plantillas)
- Bootstrap (opcional para estilos)

---

## 📦 Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/JohnRiverAG/gestion-usuarios.git
   cd gestion-usuarios

python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

2. **Crear y activar entorno virtual:**
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt

4. **Aplicar migraciones:**
   ```bash
   python manage.py makemigrations usuarios
   python manage.py migrates

5. **Ejecutar servidor:**
   ```bash
   python manage.py runserver

6. **Acceder a la aplicación:**
   Abre tu navegador en http://localhost:8000


🔐 Seguridad
Protección CSRF activada

Autenticación basada en sesiones

Validación de formularios


📄 Créditos
Desarrollado por John Arango
Licencia: MIT

📬 Contacto
¿Tienes dudas o sugerencias? 
📧 Email: johnunivalle@gmail.com
🐙 GitHub: https://github.com/JohnRiverAG