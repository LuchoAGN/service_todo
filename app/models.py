from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(150), unique=True, index=True, nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    todos = relationship("Todo", back_populates="owner")

class Todo(Base):
    __tablename__ = "todo"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500), nullable=True)
    is_completed = Column(Boolean, default=False)
    due_date = Column(Date)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="todos")