from models.constants.truck_specs import TruckBrand, TruckStatus, TruckSpecs
from errors.truck_full import TruckFullError
from models.package import Package
from models.route import Route
from datetime import datetime


class Truck:
    TRUCK_ID = 1000

    def __init__(self):
        self._truck_id = self.create_id()
        self._brand = self.validate_brand(self._truck_id)
        self._status = TruckStatus.FREE
        self._route = list[Route]
        self._packages: list = []
        self._speed = 87
        self._capacity = self.validate_capacity()
        self._range = self.validate_range()

    @property
    def brand(self):
        return self._brand

    @property
    def truck_id(self):
        return self._truck_id

    # @property
    # def route(self):
    #     return tuple(self._route)

    @property
    def packages(self):
        return tuple(self._packages)

    @property
    def capacity(self):
        return self._capacity

    @property
    def range(self):
        return self._range

    def create_id(self):
        Truck.TRUCK_ID += 1
        return Truck.TRUCK_ID

    # def capacity_left(self): закоментирано от Трифон, защото май няма да ни трябва
    #     total_packages_weight = sum(package.weight for package in self.packages)
    #     return (self._capacity - total_packages_weight)

    def load_package(self, package: Package):
        if self.capacity_left() < package.weight:
            raise TruckFullError

        self._packages.append(package)
        package.time_loaded(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        if self.capacity_left() == 0:
            self._status = TruckStatus.FULL

    def unload_package(self, package: Package):
        if self._status == TruckStatus.FULL:
            self._packages.remove(package)
            package.time_delivered(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self._status = TruckStatus.FREE
        else:
            self._packages.remove(package)
            package.time_delivered(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def validate_brand(self, current_id):
        if current_id < 1011:
            return TruckBrand.SCANIA

        elif 1011 <= current_id < 1026:
            return TruckBrand.MAN

        else:
            return TruckBrand.ACTROSS

    def validate_capacity(self):
        if self._brand == TruckBrand.SCANIA:
            return TruckSpecs.CAPACITY_SCANIA

        if self._brand == TruckBrand.MAN:
            return TruckSpecs.CAPACITY_MAN

        if self._brand == TruckBrand.ACTROSS:
            return TruckSpecs.CAPACITY_ACTROSS

    def validate_range(self):
        if self._brand == TruckBrand.SCANIA:
            return TruckSpecs.MAX_RANGE_SCANIA

        if self._brand == TruckBrand.MAN:
            return TruckSpecs.MAX_RANGE_MAN

        if self._brand == TruckBrand.ACTROSS:
            return TruckSpecs.MAX_RANGE_ACTROSS

    def __str__(self) -> str:
        return (
            f"Brand: {self.brand}\nId: {self.truck_id}\nPackages: {len(self.packages)}"
        )
