# app/api/v1/endpoints/books.py
import uuid
from fastapi import APIRouter
from typing import List
from ....schemas.github import GithubResponse, GithubCreate
from ....db.database import database

router = APIRouter()
@router.post("/", response_model=GithubResponse)
async def insert_github(item: GithubCreate):
    query = """
    INSERT INTO github (s_id, s_title, s_full_name, s_desc, s_url, b_forl, s_created_at, s_updated_at)
    VALUES (:s_id, :s_title, :s_full_name, :s_desc, :s_url, :b_forl, :s_created_at, :s_updated_at)
    RETURNING s_id, s_title, s_full_name, s_desc, s_url, b_forl, s_created_at, s_updated_at
    """

    values = {
        "s_id": str(uuid.uuid4()),
        "s_title": item.name,
        "s_full_name": item.full_name,
        "s_desc": item.description or "",
        "s_url": item.html_url,
        "b_fork": item.fork,
        "s_created_at": item.created_at,
        "s_updated_at": item.updated_at,
    }
    inserted = await database.fetch_one(query=query, values=values)
    return inserted

@router.get("/", response_model=List[GithubResponse])
async def get_github_list():
    query = "SELECT * FROM github"
    return await database.fetch_all(query=query)

@router.post("/batch", response_model=List[GithubResponse])
async def insert_github_bulk(items: List[GithubCreate]):
    query = """
    INSERT INTO github (s_id, s_title, s_full_name, s_desc, s_url, b_fork, s_created_at, s_updated_at)
    VALUES (:s_id, :s_title, :s_full_name, :s_desc, :s_url, :b_fork, :s_created_at, :s_updated_at)
    RETURNING s_id, s_title, s_full_name, s_desc, s_url, b_fork, s_created_at, s_updated_at
    """

    values = [
        {
            "s_id": str(uuid.uuid4()),
            "s_title": item.name,
            "s_full_name": item.full_name,
            "s_desc": item.description or "",
            "s_url": item.html_url,
            "b_fork": item.fork,
            "s_created_at": item.created_at,
            "s_updated_at": item.updated_at,
        }
        for item in items
    ]

    inserted = await database.execute_many(query=query, values=values)
    return inserted