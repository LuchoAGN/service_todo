from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime

# Esquema Base para Todo
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = Field(default=False)
    due_date: Optional[date] = None

# Esquema para Crear Todo
class TodoCreate(TodoBase):
    pass

# Esquema para Actualizar Todo
class TodoUpdate(TodoBase):
    pass

# Esquema para Leer Todo
class Todo(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True