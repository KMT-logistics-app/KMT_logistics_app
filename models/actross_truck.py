from truck import Truck
from constants.truck_specs import TruckBrand, TruckStatus

class Actross(Truck):
    ID_ACTROSS = 1025
    CAPACITY = 26000
    MAX_RANGE = 13000

    def __init__(self):
        self._brand = TruckBrand.ACTROSS
        self._truck_id = self.create_id()
        self._status = TruckStatus.FREE
        self._capacity = Actross.CAPACITY
        self._mileage = Actross.MAX_RANGE
    def create_id(self):
        Actross.ID_ACTROSS += 1
        return Actross.ID_ACTROSS
    

# trucks = {}

# for i in range(1, 16):
#     truck = Actross()
#     trucks[i] = truck.truck_id

# for num, id in trucks.items():
#     print(f'Truck: {num} ----- ID: {id}')