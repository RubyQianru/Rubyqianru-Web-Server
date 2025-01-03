from fastapi import APIRouter, Query
from typing import List
from ....db.mongodb import crypto_collection
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta


router = APIRouter()


@router.get("/")
async def get_all_price_list(symbol: str = Query(default="BTC", description="Coin symbol")):
   query = {"symbol": symbol}
   cursor = list(crypto_collection.find(query)) 
   for item in cursor:
      item["_id"] = str(item["_id"])
      if 'time' in item:
         item['time'] = str(item['time'])
      if 'timestamp' in item:
         item['timestamp'] = str(item['timestamp'])
   return JSONResponse(content=cursor)


# GET all available coins and their latest data
@router.get("/coin_list")
async def get_coin_list():
   pipeline = [
      {
         "$group": {
               "_id": "$symbol",
               "latest_data": {"$last": "$$ROOT"}
         }
      },
      {
         "$project": {
               "symbol": "$_id",
               "name": "$latest_data.name",
               "price": "$latest_data.price",
               "dayHigh": "$latest_data.dayHigh",
               "dayLow": "$latest_data.dayLow",
               "open": "$latest_data.open",
               "volume": "$latest_data.volume",
               "time": "$latest_data.time",
               "_id": 0
         }
      },
      {
         "$sort": {"volume": -1}
      }
   ]

   data = list(crypto_collection.aggregate(pipeline))

   for item in data:
      if 'time' in item:
         item['time'] = item['time'].isoformat() + 'Z'
      if 'timestamp' in item:
         item['timestamp'] = str(item['timestamp'])

   return JSONResponse(content=data)


# GET crypto data from the last n days
@router.get("/days")
async def get_price_list_by_days(
   symbol: str = Query(default="BTC", description="Coin symbol"),
   days: int = Query(default=7, description="Number of days to fetch data for")
   ):

   query = {"symbol": symbol}
   if days is not None:
      end_date = datetime.now()
      start_date = end_date - timedelta(days=days)
      query["time"] = {
         "$gte": start_date,
         "$lte": end_date
      }
   
   data = list(crypto_collection.find(query).sort('timestamp', 1))
   for item in data:
      item["_id"] = str(item["_id"])
      if 'time' in item:
         item['time'] = item['time'].isoformat() + 'Z'
      if 'timestamp' in item:
         item['timestamp'] = str(item['timestamp'])
   
   return JSONResponse(content=data)


@router.get("/weekly_summary")
async def get_weekly_summary(symbol: str = Query(default="BTC", description="Coin symbol"),):
   end_date = datetime.now()
   start_date = end_date - timedelta(days=7)

   pipeline = [
      {
         "$match": {
            "symbol": symbol,
            "time": {
               "$gte": start_date,
               "$lte": end_date
            }
         }
      },
      {
         "$group": {
            "_id": {
               "$dateToString": {
                  "format": "%Y-%m-%d",
                  "date": "$time"
               }
            },
            "first_data": {"$first": "$$ROOT"},
            "last_data": {"$last": "$$ROOT"}
         }
      },
      {
         "$sort": {"_id": 1}
      }
   ]

   data = list(crypto_collection.aggregate(pipeline))

   for item in data:
      item["_id"] = str(item["_id"])
      if 'time' in item:
         item['time'] = item['time'].isoformat() + 'Z'
      if 'timestamp' in item:
         item['timestamp'] = str(item['timestamp'])

   return JSONResponse(content=data)
