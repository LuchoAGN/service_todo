from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.scheme_todo import Todo, TodoCreate, TodoUpdate
from app.controllers.todo_controller import get_todos, get_todo, create_todo, update_todo, delete_todo
from app.controllers.auth_controller import get_current_user

router = APIRouter()

@router.get("/", response_model=List[Todo])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return get_todos(db=db, owner_id=current_user.id, skip=skip, limit=limit)

@router.get("/{todo_id}", response_model=Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return get_todo(db=db, owner_id=current_user.id, todo_id=todo_id)

@router.post("/", response_model=Todo)
def create_new_todo(todo: TodoCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return create_todo(db=db, owner_id=current_user.id, todo=todo)

@router.put("/{todo_id}", response_model=Todo)
def update_existing_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return update_todo(db=db, owner_id=current_user.id, todo_id=todo_id, todo=todo)

@router.delete("/{todo_id}", response_model=Todo)
def delete_existing_todo(todo_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return delete_todo(db=db, owner_id=current_user.id, todo_id=todo_id)