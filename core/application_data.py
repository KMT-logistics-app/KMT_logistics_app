from models.package import Package
from models.truck import Truck
from models.route import Route


class ApplicationData:
    def __init__(self):
        self._trucks: list[Truck] = []
        self._packages: list[Package] = []
        self._routes: list[Route] = []

    @property
    def packages(self):
        return tuple(self._packages)

    def create_package(self, start_location, delivery_adress, weight, customer_info):
        new_package = Package(start_location, delivery_adress, weight, customer_info)
        self._packages.append(new_package)
        # if self.find_package_by_id(new_package.id) is None:
        #     raise ValueError("Package %s already exists")

        return new_package

    def find_package_by_id(self, pack_id):
        for pack in self._packages:
            if pack.id == pack_id:
                return pack

        return None

    def find_truck_by_id(self, truck_id):
        for truck in self._trucks:
            if truck.truck_id == truck_id:
                return truck
        return None

    def create_delivery_route(self, starting_point, delivery_adress):
        new_route = Route(starting_point, delivery_adress)
        self._routes.append(new_route)
        return new_route

    def find_route_by_locations(self, start_location, delivery_adress):
        for route in self._routes:
            #Да се види дали не трябв да ила стартова локация и крайна в самия клас или точно правилоно съм го разбрал, и е направено чрез пакинг
            if route.route_points == start_location and route.route_points == delivery_adress:
                return route
        raise ValueError("Route not found")

    def find_route_by_id(self, route_id):
        for route in self._routes:
            if route.route_id == route_id:
                return route
        return None
