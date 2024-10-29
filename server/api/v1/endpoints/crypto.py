from fastapi import APIRouter
from typing import List
from ....db.mongodb import crypto_collection
from fastapi.responses import JSONResponse
import json

router = APIRouter()

@router.get("/")
async def get_crypto_list():
    query = {}
    cursor = list(crypto_collection.find(query)) 
    for item in cursor:
      item["_id"] = str(item["_id"])
      if 'time' in item:
         item['time'] = str(item['time'])
      if 'timestamp' in item:
         item['timestamp'] = str(item['timestamp'])
    # print(cursor)
    return JSONResponse(content=cursor)

