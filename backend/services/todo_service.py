from sqlmodel import Session, select
from fastapi import HTTPException, status
from models import Todo
from schemas import TodoCreate, TodoUpdate, TodoRead


def create_todo_service(session: Session, todo_data: TodoCreate, user_id: int):
    new_todo = Todo(
        title=todo_data.title,
        description=todo_data.description,
        owner_id=user_id
    )

    session.add(new_todo)
    session.commit()
    session.refresh(new_todo)

    return new_todo


def get_todos_service(session: Session, user_id: int):
    return session.exec(
        select(Todo).where(Todo.owner_id == user_id)
    ).all()


def update_todo_service(session: Session, todo_id: int, todo_data: TodoUpdate, user_id: int):
    todo = session.get(Todo, todo_id)

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )

    if todo.owner_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this todo"
        )

    if todo_data.title is not None:
        todo.title = todo_data.title

    if todo_data.description is not None:
        todo.description = todo_data.description

    if todo_data.completed is not None:
        todo.completed = todo_data.completed

    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo


def delete_todo_service(session: Session, todo_id: int, user_id: int):
    todo = session.get(Todo, todo_id)

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )

    if todo.owner_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this todo"
        )

    session.delete(todo)
    session.commit()

    return {"message": "Todo deleted"}
