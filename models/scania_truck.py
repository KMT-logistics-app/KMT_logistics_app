from truck import Truck
from constants.truck_specs import TruckBrand, TruckStatus

class Scania(Truck):
    ID_SCANIA = 1000
    CAPACITY = 42000
    MAX_RANGE = 8000
    def __init__(self) -> None:
        self._brand = TruckBrand.SCANIA
        self._truck_id = self.create_id()
        self._status = TruckStatus.FREE
        self._capacity = Scania.CAPACITY
        self._mileage = Scania.MAX_RANGE


    def create_id(self):
        Scania.ID_SCANIA += 1
        return Scania.ID_SCANIA
    