from fastapi import FastAPI
from app.routers import auth, todo
from app.database import engine, Base

# Crea todas las tablas
Base.metadata.create_all(bind=engine)


description = """
Un backend para una aplicación de gestión de tareas (Todo) desarrollado con FastAPI y SQLAlchemy, utilizando MySQL para 
la base de datos. Esta API proporciona funcionalidades de autenticación, manejo de tareas y gestión de usuarios. 🚀

Este proyecto es un backend para una aplicación de gestión de tareas. Proporciona endpoints para:

- Registro y autenticación de usuarios
- Gestión de tareas (crear, leer, actualizar y eliminar)
- Recuperación de información del usuario actual
"""

app = FastAPI( title="Service ToDo",
    description=description,
    summary="My favorite basic service",
    version="0.0.1",
    terms_of_service="https://github.com/LuchoAGN/service_todo?tab=MIT-1-ov-file",
    contact={
        "name": "Lucho AGN",
        "url": "https://luchoagn.dev/",
        "email": "contact@luchoagn.dev",
    },
    license_info={
        "name": "MIT license",
        "url": "https://opensource.org/license/mit",
    },)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(todo.router, prefix="/todos", tags=["todos"])