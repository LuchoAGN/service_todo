from fastapi import FastAPI
from app.routers import auth, todo
from app.database import engine, Base

# Crea todas las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(todo.router, prefix="/todos", tags=["todos"])