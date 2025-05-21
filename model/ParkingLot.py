from typing import Dict


class ParkingLot:
    parkId: str
    name_en: str
    name_tc: str
    name_sc: str
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
