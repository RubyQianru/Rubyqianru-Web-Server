# app/api/v1/api.py
from fastapi import APIRouter
from .endpoints import jobs, github, crypto

v1_api_router = APIRouter()

v1_api_router.include_router(
  jobs.router, 
  prefix="/jobs", 
  tags=["jobs"]
  )

v1_api_router.include_router(
  github.router, 
  prefix="/github", 
  tags=["github"]
  )

v1_api_router.include_router(
  crypto.router, 
  prefix="/crypto", 
  tags=["crypto"]
  )

v1_api_router.include_router(
  crypto.router, 
  prefix="/twitter", 
  tags=["twitter"]
  )