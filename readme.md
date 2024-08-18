# **Todo API Backend**

Un backend para una aplicación de gestión de tareas (Todo) desarrollado con FastAPI y SQLAlchemy, utilizando MySQL para la base de datos. Esta API proporciona funcionalidades de autenticación, manejo de tareas y gestión de usuarios.

## **Índice**

- [Descripción](#descripción)
- [Tecnologías](#tecnologías)
- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribución](#contribución)
- [Licencia](#licencia)

## **Descripción**

Este proyecto es un backend para una aplicación de gestión de tareas. Proporciona endpoints para:

- Registro y autenticación de usuarios
- Gestión de tareas (crear, leer, actualizar y eliminar)
- Recuperación de información del usuario actual

## **Tecnologías**

- **FastAPI**: Framework web moderno y rápido para construir APIs con Python 3.6+ basado en estándar de Python tipo hints.
- **SQLAlchemy**: ORM (Object Relational Mapper) para manejar bases de datos SQL en Python.
- **MySQL**: Sistema de gestión de bases de datos relacional.
- **PassLib**: Biblioteca para el manejo de contraseñas.
- **PyJWT**: Biblioteca para generar y verificar tokens JWT.

## **Características**

- **Autenticación JWT**: Seguridad para las rutas protegidas mediante tokens JWT.
- **CRUD de Tareas**: Crear, leer, actualizar y eliminar tareas.
- **Registro y Login**: Registro de nuevos usuarios y autenticación con nombre de usuario y contraseña.
- **Validación de Datos**: Utiliza Pydantic para la validación de datos en las solicitudes.

## **Instalación**

### **Requisitos Previos**

- Python 3.7 o superior
- MySQL Server
- `pip` para instalar dependencias

### **Pasos para la Instalación**

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/tu_usuario/todo-api-backend.git
   cd todo-api-backend
   ```

2. **Clonar el Repositorio**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. **Instalar Dependencias**
