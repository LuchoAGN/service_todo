from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models
from app.schemas import scheme_todo

def get_todos(db: Session, owner_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Todo).filter(models.Todo.owner_id == owner_id).offset(skip).limit(limit).all()

def get_todo(db: Session, owner_id: int, todo_id: int):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id == owner_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

def create_todo(db: Session, owner_id: int, todo: scheme_todo.TodoCreate):
    db_todo = models.Todo(**todo.dict(), owner_id=owner_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, owner_id: int, todo_id: int, todo: scheme_todo.TodoUpdate):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id == owner_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    for key, value in todo.dict(exclude_unset=True).items():
        setattr(db_todo, key, value)
    
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, owner_id: int, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id == owner_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(db_todo)
    db.commit()
    return db_todo