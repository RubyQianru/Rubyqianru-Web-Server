# app/schemas/book.py
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    price: float

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    price: float

    class Config:
        orm_mode = True