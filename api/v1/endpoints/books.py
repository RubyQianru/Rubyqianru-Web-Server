# app/api/v1/endpoints/books.py
from fastapi import APIRouter, Depends
from typing import List
from server.schemas.book import BookCreate, BookResponse
from server.db.database import database, books

router = APIRouter()

@router.post("/", response_model=BookResponse)
async def create_book(book: BookCreate):
    query = books.insert().values(title=book.title, author=book.author, price=book.price)
    last_book_id = await database.execute(query)

    query = books.select().where(books.c.id == last_book_id)
    inserted_book = await database.fetch_one(query)
    return inserted_book

@router.get("/", response_model=List[BookResponse])
async def get_books():
    query = books.select()
    return await database.fetch_all(query)