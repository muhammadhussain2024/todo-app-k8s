from pydantic import BaseModel, Field, field_validator
from typing import Optional


# -------- USER --------
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)


class UserRead(BaseModel):
    id: int
    username: str


# -------- TODO --------
class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    
    @field_validator('title')
    @classmethod
    def title_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Title cannot be empty or only whitespace')
        return v.strip()


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None


class TodoRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    owner_id: int
    
    class Config:
        from_attributes = True
