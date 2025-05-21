from fastapi import FastAPI, HTTPException
import json
from model.ParkingLot import ParkingLot
from typing import List

app = FastAPI()

parkingLots : List[ParkingLot] = []

file = open("data/parkingLot.json")
dataJson = file.read()
data = json.loads(dataJson)
for item in data:
    obj = ParkingLot(**item)
    parkingLots.append(obj)



@app.get("/")
async def root():
    return {"message":"Hello world"}

@app.get("/parkingLots/{parkingLotId}")
async def getParkingLot(parkingLotId:str):
    print("Finding lot "+parkingLotId)
    foundParkingLots = list(filter(lambda x: x.park_id == parkingLotId, parkingLots ))

    if(not any(foundParkingLots)):
        raise HTTPException(status_code=404, detail = "Item not found")
    return foundParkingLots

@app.get("/parkingLots/")
async def getParkingLots(page: int = 1, limit : int = 10):
    start_index = (page - 1) * limit
    end_index = start_index + limit
    return parkingLots[start_index:end_index]
