# app/api/v1/api.py
from fastapi import APIRouter
from .endpoints import jobs

api_router = APIRouter()
api_router.include_router(
  jobs.router, 
  prefix="/jobs", 
  tags=["jobs"]
  )