# app/main.py
from fastapi import FastAPI
from server.api.v1.api import api_router
from server.db.database import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(api_router, prefix="/api/v1")