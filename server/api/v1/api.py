# app/api/v1/api.py
from fastapi import APIRouter
from .endpoints import github, crypto, twitter, report

v1_api_router = APIRouter()

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
  twitter.router, 
  prefix="/twitter", 
  tags=["twitter"]
  )

v1_api_router.include_router(
  report.router, 
  prefix="/report", 
  tags=["report"]
  )