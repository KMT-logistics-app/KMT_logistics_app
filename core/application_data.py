from models.package import Package
from models.truck import Truck
from models.route import Route
from models.constants.package_status import Package_status
from models.constants.cities import Cities


class ApplicationData:
    def __init__(self):
        self._trucks: list[Truck] = []
        self._packages: list[Package] = []
        self._routes: list[Route] = []

    @property
    def packages(self):
        return tuple(self._packages)

    @property
    def trucks(self):
        return self._trucks

    @property
    def routes(self):
        return self._routes

    def find_free_truck_by_location(self, location: str):
        trucks = []
        for truck in self._trucks:
            if truck.status == "free" and truck.location == location:
                trucks.append(truck)

        if len(trucks) == 0:
            return f"No free trucks in {location}"

        return trucks

    def create_package(self, start_location, delivery_adress, weight, customer_info):
        new_package = Package(start_location, delivery_adress, weight, customer_info)
        self._packages.append(new_package)
        return new_package

    def create_truck(self):
        truck = Truck()
        self._trucks.append(truck)
        return truck

    def create_route(self, route_points, departure_time):
        new_route = Route(route_points, departure_time)
        self._routes.append(new_route)
        return new_route

    def calculate_distance(self, A, B) -> int:
        for current, next_city in Cities.DISTANCES.items():
            if current == A:
                for i in range(len(next_city)):
                    if B == next_city[i][0]:
                        return next_city[i][1]

    def find_package_by_id(self, pack_id):
        for pack in self._packages:
            if pack._id == pack_id:
                return pack

    def find_truck_by_id(self, truck_id):
        for truck in self._trucks:
            if truck.truck_id == truck_id:
                return truck

    def find_route_by_locations(self, start_location, delivery_adress):
        found = []
        for route in self._routes:
            if (
                start_location in route.route_points
                and delivery_adress in route.route_points
            ):
                start_idx = route.route_points.index(start_location)
                if delivery_adress in route.route_points[start_idx:]:
                    found.append(route)

        return found if len(found) > 0 else None

    def find_route_by_id(self, route_id):
        for route in self._routes:
            if route.route_id == route_id:
                return route
        return None

    def view_routes_in_progress(self):
        """
        Only a menager should be able to perform this task!
        """
        temp_result = []
        for route in self._routes:
            if route.status == Route.IN_PROGRESS:
                temp_result.append(route)

        result_to_return = []
        for r in temp_result:
            result_to_return.append(str(r))

        return "\n".join(result_to_return)

    # def view_locations(self):
    #     towns = {
    #         "SYDNEY": [],
    #         "MELBOURNE": [],
    #         "ADELAIDE": [],
    #         "ALICE SPRINGS": [],
    #         "BRISBANE": [],
    #         "DARWIN": [],
    #         "PERTH": [],
    #     }
    #     for package in self._packages:
    #         if package.current_location in Cities.cities:
    #             towns[package.current_location.upper()].append(package.weight)

    #     output = []

    #     for key, value in towns.items():
    #         output.append(
    #             f"{key.capitalize()} has packages with total weight {sum(value)}kg."
    #         )

    #     return "\n".join(output)

    # def view_location(self, location):
    #     city_packages = []
    #     for package in self._packages:
    #         if (
    #             package.current_location.upper() == location.upper()
    #             and package.status == Package_status.ACCEPTED
    #         ):
    #             city_packages.append(package)

    #     towns = {
    #         "SYDNEY": [],
    #         "MELBOURNE": [],
    #         "ADELAIDE": [],
    #         "ALICE SPRINGS": [],
    #         "BRISBANE": [],
    #         "DARWIN": [],
    #         "PERTH": [],
    #     }

    #     for package in city_packages:
    #         towns[f"{package.end_location.upper()}"].append(package.weight)

    #     output = [f"{location.captalize()} has packages for these locations:"]

    #     for key, value in towns.items():
    #         output.append(
    #             f"{key.capitalize()} has packages with total weight {sum(value)}kg."
    #         )

    #     return "\n".join(output)
