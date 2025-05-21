from typing import Dict


class ParkingLotRealTime:
    parkId: str
    privateCar: object
    LGV: object
    HGV: object
    motorCycle: object

    def __init__(self, park_Id:str ):
        self.parkId = park_Id

def ParkingLotRealTime_decoder(dct):
    if "__type__" in dct and dct["__type__"] == "ParkingLotRealTime":
        return ParkingLotRealTime(dct["park_id"])
    return dct