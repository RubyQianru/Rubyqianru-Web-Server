# app/api/v1/endpoints/books.py
from fastapi import APIRouter
from typing import List
from ....schemas.job import JobCreate, JobResponse
from ....db.database import database
import uuid

router = APIRouter()

@router.post("/", response_model=JobResponse)
async def create_job(job: JobCreate):
    query = """
    INSERT INTO jobs (s_id, s_title, s_company, s_url, b_apply, s_tag, s_time)
    VALUES (:s_id, :s_title, :s_company, :s_url, :b_apply, :s_tag, NOW())
    RETURNING s_id, s_title, s_company, s_url, b_apply, s_tag, s_time
    """
    values = {
        "s_id": str(uuid.uuid4()),
        "s_title": job.s_title, 
        "s_company": job.s_company,
        "s_url": job.s_url,
        "b_apply": job.b_apply,
        "s_tag": job.s_tag
    }
    inserted = await database.fetch_one(query=query, values=values)
    return inserted

@router.get("/", response_model=List[JobResponse])
async def get_job():
    query = "SELECT s_id, s_title, s_company, s_url, b_apply, s_tag, s_time FROM jobs"
    return await database.fetch_all(query=query)