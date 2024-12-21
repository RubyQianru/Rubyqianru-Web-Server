from fastapi import APIRouter, Query
from typing import List
from ....db.mongodb import report_collection
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
import json

router = APIRouter()


@router.get("/")
async def get_all_report_list(symbol: str = Query(default="BTC", description="Coin symbol")):
   query = {"symbol": symbol}
   cursor = list(report_collection.find(query)) 
   for item in cursor:
      item["_id"] = str(item["_id"])
      if 'time' in item:
         item['time'] = str(item['time'])
      if 'timestamp' in item:
         item['timestamp'] = str(item['timestamp'])
   return JSONResponse(content=cursor)


# Get available reports from the last few days
@router.get("/days")
async def get_report_list(
   symbol:str = Query(default="BTC", description="Coin symbol"),
   days: int = Query(default=1, description="Number of days to fetch data for")
   ):

   query = {"symbol": symbol}
   if days is not None:
      end_date = datetime.now()
      start_date = end_date - timedelta(days=days)
      query["time"] = {
         "$gte": start_date,
         "$lte": end_date
      }

   data = list(report_collection.find(query).sort('time', -1))
   for item in data:
      item["_id"] = str(item["_id"])
      if 'time' in item:
         item['time'] = str(item['time'])

   return JSONResponse(content=data)
