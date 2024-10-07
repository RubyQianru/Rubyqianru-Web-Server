# app/api/v1/api.py
from fastapi import APIRouter
from .endpoints import books

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])