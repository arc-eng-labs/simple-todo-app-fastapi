from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List

from .database import SessionLocal, engine, Base
from . import crud, models, schemas

# Create tables in the SQLite database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mount the static directory to serve index.html, css, and js
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos", response_model=List[schemas.TodoRead])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@app.post("/todos", response_model=schemas.TodoRead)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

@app.put("/todos/{todo_id}", response_model=schemas.TodoRead)
def update_todo_item(todo_id: int, todo_update: schemas.TodoUpdate, db: Session = Depends(get_db)):
    updated_todo = crud.update_todo(db, todo_id, todo_update)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@app.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int, db: Session = Depends(get_db)):
    success = crud.delete_todo(db, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
