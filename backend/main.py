from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, SQLModel
from typing import List

from database import engine, get_session
from schemas import UserCreate, UserRead, TodoCreate, TodoUpdate, TodoRead
from services.auth_service import signup_service, login_service
from services.todo_service import (
    create_todo_service,
    get_todos_service,
    update_todo_service,
    delete_todo_service
)

from dependencies import get_current_user
from models import User


app = FastAPI(
    title="Todo API",
    description="A simple todo application with user authentication",
    version="1.0.0"
)


# -------- CREATE TABLES --------
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# -------- ROOT --------
@app.get("/")
def root():
    return {"message": "Todo API Running"}


# -------- AUTH --------
@app.post("/signup")
def signup(user: UserCreate, session: Session = Depends(get_session)):
    return signup_service(session, user)


@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    return login_service(session, form_data)


@app.get("/me", response_model=UserRead)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


# -------- TODOS --------
@app.post("/todos", response_model=TodoRead)
def create_todo(
    todo: TodoCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return create_todo_service(session, todo, current_user.id)


@app.get("/todos", response_model=List[TodoRead])
def get_todos(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return get_todos_service(session, current_user.id)


@app.put("/todos/{todo_id}", response_model=TodoRead)
def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return update_todo_service(session, todo_id, todo, current_user.id)


@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return delete_todo_service(session, todo_id, current_user.id)
