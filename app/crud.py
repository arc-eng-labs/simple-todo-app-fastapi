from sqlalchemy.orm import Session
from . import models, schemas


def get_todos(db: Session):
    return db.query(models.Todo).all()


def create_todo(db: Session, todo: schemas.TodoCreate):
    new_todo = models.Todo(title=todo.title, is_completed=todo.is_completed)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def update_todo(db: Session, todo_id: int, todo_update: schemas.TodoUpdate):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        return None

    if todo_update.title is not None:
        db_todo.title = todo_update.title
    if todo_update.is_completed is not None:
        db_todo.is_completed = todo_update.is_completed

    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        return False
    db.delete(db_todo)
    db.commit()
    return True
