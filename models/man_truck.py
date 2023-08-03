from truck import Truck
from constants.truck_specs import TruckBrand, TruckStatus

class Man(Truck):
    ID_MAN = 1010
    CAPACITY = 37000
    MAX_RANGE = 10000
    def __init__(self) -> None:
        self._brand = TruckBrand.MAN
        self._truck_id = self.create_id()
        self._status = TruckStatus.FREE
        self._capacity = Man.CAPACITY
        self._mileage = Man.MAX_RANGE


    def create_id(self):
        Man.ID_MAN += 1
        return Man.ID_MAN
