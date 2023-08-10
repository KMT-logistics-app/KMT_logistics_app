from models.constants.cities import Cities
from datetime import datetime, timedelta
from models.constants.package_status import Package_status
from models.package import Package
from models.truck import Truck


class Route:
    ROUTE_ID = 0
    IN_PROGRESS = 'in progress'
    PENDING = 'pending'

    def __init__(self, *args) -> None:
        self.route_points = args[0]
        self.departure_time = args[-1]
        self._id = self.create_id()
        self._distance = self.total_distance(self.route_points)

        if self._departure_time < datetime.now():
            self._status = self.IN_PROGRESS
        else:
            self._status = self.PENDING
        
        self.trucks: list[Truck] = []
        self._packages: list[Package] = []


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
        return self._status

    # @status.setter
    # def status(self):
    #     if self._departure_time < datetime.now():
    #         self._status = self.IN_PROGRESS
    #     else:
    #         self._status = self.PENDING


    @property
    def route_id(self):
        return self._id

    @property
    def distance(self):
        return self._distance


    def assign_package(self, pack: Package):
        pack._status = Package_status.LOADED
        self._packages.append(pack)


    def assign_truck(self, truck: Truck):
        self.trucks.append(truck)


    def calculate_estimated_time(self, lst):
        '''
            Currently this method returns the estimated time of arrival 
            between the starting point and the final point of the route.
            Probably it should give information about the eta between the 
            route's points so we can use the info in the next_stop method?
        '''
        eta = self.departure_time
        for city in lst[:-1]:
            for current, next_city in Cities.DISTANCES.items():
                if current == city:
                    city_idx = lst.index(city)
                    for i in range(len(next_city)):
                        if lst[city_idx + 1] == next_city[i][0]:
                            eta += timedelta(hours=next_city[i][1] / 87)
                            break
                    break

        return eta


    def create_id(self):
        Route.ROUTE_ID += 1
        return Route.ROUTE_ID


    def packages_weight(self):
        weight_sum = 0
        for package in self._packages:
            weight_sum += package.weight
        return weight_sum


    def trucks_capacity(self):
        all_trucks_capacity = 0
        for truck in self.trucks:
            all_trucks_capacity += truck.capacity
        result = all_trucks_capacity - self.packages_weight()
        if result > 0:
            return result
        else:
            return 0


    def total_distance(self, lst):
        total = 0

        for city in lst[:-1]:
            for current, next_city in Cities.DISTANCES.items():
                if current == city:
                    city_idx = lst.index(city)
                    for i in range(len(next_city)):
                        if lst[city_idx + 1] == next_city[i][0]:
                            total += next_city[i][1]
                            break
                    break

        return total
    

    def next_stop(self):
        '''
            Should return the next city, based on the time of day. 
            We can probably get the info for the next stop from the 
            calculate_estimated_time method?
        '''
        raise NotImplementedError


    def __str__(self) -> str:
        new_line = "\n"
        return f'Route ID: {self._id}\
        {new_line}  Total distance: {self._distance}km\
        {new_line}  Route details: {" -> ".join(self.route_points)}\
        {new_line}  Packages: {len(self._packages)} with total weight {self.packages_weight()}kgs\
        {new_line}  Next stop {self.next_stop()}'

# route = ["Alice Springs", "Adelaide", "Melbourne", "Sydney", "Brisbane"]
# new_route = Route(route)

# print(str(new_route))
# hours = new_route.calculate_estimated_time(route)
