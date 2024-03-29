from models.constants.cities import Cities
from datetime import datetime, timedelta
from models.constants.package_status import Package_status
from models.package import Package
from models.truck import Truck


class Route:
    ROUTE_ID = 0
    IN_PROGRESS = "in progress"
    PENDING = "pending"
    FINISHED = "finished"

    def __init__(self, *args) -> None:
        self.route_points = args[0]
        self.departure_time = args[-1]
        self._id = self.create_id()
        self._distance = self.total_distance(self.route_points)
        self.truck: Truck = None
        self._packages: list[Package] = []
        self._status = self.PENDING

    @property
    def route_points(self):
        return self._route_points

    @route_points.setter
    def route_points(self, value):
        self._route_points = value

    @property
    def departure_time(self):
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value):
        if not isinstance(value, datetime):
            raise TypeError
        self._departure_time = value

    @property
    def status(self):
        if datetime.now() > self.calculate_estimated_time():
            return self.FINISHED
        if datetime.now() < self._departure_time:
            return self.PENDING
        return self.IN_PROGRESS

    
    @property
    def route_id(self):
        return self._id

    @property
    def distance(self):
        return self._distance
    
    @property
    def packages(self):
        return tuple(self._packages)

    def assign_package(self, pack: Package):
        pack._status = Package_status.ASSIGNED
        pack.estimated_arrival_time = self.calculate_estimated_time()
        self._packages.append(pack)

    def assign_truck(self, truck: Truck):
        self.truck = truck

    def calculate_estimated_time(self):
        estimated_arrival_time = self.departure_time
        
        for city in self.route_points[:-1]:
            for current, next_city in Cities.DISTANCES.items():
                if current == city:
                    city_idx = self._route_points.index(city)
                    for i in range(len(next_city)):
                        if self.route_points[city_idx + 1] == next_city[i][0]:
                            estimated_arrival_time += timedelta(hours=next_city[i][1] / 87)
                            break
                    break

        return estimated_arrival_time

    def create_id(self):
        Route.ROUTE_ID += 1
        return Route.ROUTE_ID

    def packages_weight(self):
        weight_sum = 0
        for package in self._packages:
            weight_sum += package.weight
        return weight_sum

    def truck_capacity(self):
        result = self.truck.capacity - self.packages_weight()
        if result > 0:
            return result
        else:
            return 0

    def total_distance(self, route_points: list):
        total = 0

        for city in route_points[:-1]:
            for current, next_city in Cities.DISTANCES.items():
                if current == city:
                    city_idx = route_points.index(city)
                    for i in range(len(next_city)):
                        if route_points[city_idx + 1] == next_city[i][0]:
                            total += next_city[i][1]
                            break
                    break

        return total

    def __str__(self) -> str:
        new_line = "\n"
        return f'Route ID: {self._id}\
        {new_line}  Status: {self.status}\
        {new_line}  Total distance: {self._distance}km\
        {new_line}  Route details: {" -> ".join(self.route_points)}\
        {new_line}  Packages: {len(self._packages)} with total weight {self.packages_weight()}kgs\
        {new_line}  Truck assigned: {new_line}{str(self.truck) if self.truck else None}'
