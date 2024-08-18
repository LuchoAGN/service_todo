from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Esquema para la creación de usuarios
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Esquema para la respuesta de usuario (sin contraseña)
class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

# Esquema para manejar tokens
class Token(BaseModel):
    access_token: str
    token_type: str

# Esquema para los datos dentro del token
class TokenData(BaseModel):
    username: Optional[str] = None