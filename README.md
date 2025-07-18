# 📋 Aplicación Web de Pizarra de Pendientes (ToDo)

## 📝 Descripción
Aplicación web desarrollada en Django que permite gestionar una lista de pendientes (ToDo) con funcionalidades completas de consulta y CRUD.

## 🚀 Requisitos para ejecutar el proyecto

### 1. **Software necesario**
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

### 2. **Instalación y configuración**

#### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/elchinito24/examen2.git
cd examen2
```

#### Paso 2: Crear y activar el entorno virtual
```bash
# Crear entorno virtual
python -m venv env

# Activar entorno virtual (Windows)
env\Scripts\activate

# Activar entorno virtual (Linux/Mac)
source env/bin/activate
```

#### Paso 3: Instalar dependencias
```bash
pip install django
```

#### Paso 4: Navegar al directorio del proyecto
```bash
cd projectExamen2
```

#### Paso 5: Realizar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Paso 6: Crear superusuario (obligatorio)
```bash
python manage.py createsuperuser
```
*Nota: Este paso es necesario para tener usuarios disponibles en el formulario*

#### Paso 7: Ejecutar el servidor
```bash
python manage.py runserver
```

### 3. **Acceso a la aplicación**
- **Aplicación principal:** http://127.0.0.1:8000/
- **Panel de administración:** http://127.0.0.1:8000/admin/

## 📋 Funcionalidades implementadas

### **Listas de consulta (7 requerimientos funcionales):**
1. **Solo IDs** - `/todos/list/ids/`
2. **IDs + Títulos** - `/todos/list/id-titles/`
3. **Sin Resolver** - `/todos/list/unresolved/`
4. **Resueltos** - `/todos/list/resolved/`
5. **IDs + Usuario** - `/todos/list/id-user/`
6. **Resueltos + Usuario** - `/todos/list/resolved-user/`
7. **Sin Resolver + Usuario** - `/todos/list/unresolved-user/`

### **Operaciones CRUD:**
- ✅ **Crear** pendiente - `/todos/create/`
- ✅ **Leer** pendientes (7 vistas diferentes)
- ✅ **Actualizar** pendiente - `/todos/update/<id>/`
- ✅ **Eliminar** pendiente - `/todos/delete/<id>/`

## 🏗️ Estructura del proyecto
```
projectExamen2/
├── manage.py
├── db.sqlite3
├── projectExamen2/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── todo_app/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    └── templates/
        └── todo_app/
            ├── list_ids.html
            ├── list_id_titles.html
            ├── list_unresolved.html
            ├── list_resolved.html
            ├── list_id_user.html
            ├── list_resolved_user.html
            ├── list_unresolved_user.html
            └── todo_form.html
```

## 🔧 Comandos útiles

### Gestión de usuarios:
```bash
# Crear superusuario
python manage.py createsuperuser

# Cambiar contraseña de usuario
python manage.py changepassword nombre_usuario
```

### Gestión de base de datos:
```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Verificar configuración
python manage.py check
```

## 🎯 Notas importantes
1. **Obligatorio crear usuarios:** El formulario requiere que existan usuarios en la base de datos
2. **Navegación completa:** Todas las vistas tienen enlaces a las 7 listas requeridas
3. **Diseño responsive:** Interfaz moderna y fácil de usar
4. **Validaciones:** Confirmación de eliminación y manejo de errores

## 👨‍💻 Desarrollado por
**Alumno:** Robledo Ramirez Jorge Rafael

**Materia:** Desarrollo de Aplicaciones Móviles  
**Examen 2:** Aplicación Web ToDo con Django
