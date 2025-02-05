from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: Optional[str] = None
    is_completed: Optional[bool] = None

class TodoCreate(TodoBase):
    title: str
    is_completed: bool = False

class TodoUpdate(TodoBase):
    pass

class TodoRead(BaseModel):
    id: int
    title: str
    is_completed: bool

    class Config:
        orm_mode = True
