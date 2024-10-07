# app/api/v1/endpoints/books.py
from fastapi import APIRouter, Depends
from typing import List
from ....schemas.job import JobCreate, JobResponse
from ....db.database import database, jobs

router = APIRouter()

@router.post("/", response_model=JobResponse)
async def create_book(job: JobCreate):
    query = jobs.insert().values(
        title=job.title, 
        author=job.author, 
        price=job.price
        )
    last_job_id = await database.execute(query)

    query = jobs.select().where(jobs.c.id == last_job_id)
    inserted = await database.fetch_one(query)
    return inserted

@router.get("/", response_model=List[JobResponse])
async def get_books():
    query = jobs.select()
    return await database.fetch_all(query)