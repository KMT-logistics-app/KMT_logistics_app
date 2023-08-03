from constants.truck_specs import TruckBrand, TruckStatus
from package import Package
from warehouse import Warehouse


class Truck:
    def __init__(self, brand) -> None:
        self._brand = self.validate_brand(brand)
        self._truck_id = self.create_id()
        self._status = TruckStatus.FREE
        self._route: list[Warehouse] = []
        self._packages: list(Package) = []


    @property
    def brand(self):
        return self._brand


    @property
    def truck_id(self):
        return self._truck_id


    @property
    def routes(self):
        return tuple(self._route)


    @property
    def packages(self):
        return tuple(self._packages)


    def validate_brand(self, value):
        if value not in [TruckBrand.ACTROSS, TruckBrand.MAN, TruckBrand.SCANIA]:
            raise ValueError(f'Invalid brand name: {value}')
        self._brand = value


    def create_id(self):
        raise NotImplementedError('Override in derived classes.')
    

    def __str__(self) -> str:
        return f'Brand: {self.brand}\nId: {self.truck_id}\nPackages: 0'
