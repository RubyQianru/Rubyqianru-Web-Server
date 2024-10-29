# app/main.py
from fastapi import FastAPI
from server.api.v1.api import v1_api_router
from server.db.database import database
from server.core.config import settings

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(v1_api_router, prefix="/v1")