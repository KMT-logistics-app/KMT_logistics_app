from constants.truck_specs import TruckBrand, TruckStatus
from errors.truck_full import TruckFullError
from models.package import Package
from models.warehouse import Warehouse
from datetime import datetime

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
        if value not in TruckBrand.truck_brands:
            raise ValueError(f'Invalid brand name: {value}')
        self._brand = value


    def create_id(self):
        raise NotImplementedError('Override in derived classes.')
    

    def capacity_left(self):
        total_packages_weight = sum(package.weight for package in self.packages)
        return (self.CAPACITY - total_packages_weight)


    def load_package(self, package: Package):
        if self.capacity_left() + package.weight > self.CAPACITY:
            raise TruckFullError
        self._packages.append(package)
        package.time_loaded(datetime.now())
        if self.capacity_left() == 0:
            self._status = TruckStatus.FULL


    def unload_package(self, package: Package):
        if self._status == TruckStatus.FULL:
            self._packages.remove(package)
            package.time_delivered(datetime.now())
            self._status = TruckStatus.FREE
        else:
            self._packages.remove(package)
            package.time_delivered(datetime.now())

        
        # тук трябва да е минала проверка find_package_by_id, която да е върнала 
        # Package обект и тук просто да се разтовари този package от камиона


    def __str__(self) -> str:
        return f'Brand: {self.brand}\nId: {self.truck_id}\nPackages: 0'
