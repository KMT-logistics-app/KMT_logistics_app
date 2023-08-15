from models.customer import Customer
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
        self._customers: list[Customer] = []
        self.logged_in_user = None

    @property
    def packages(self):
        return tuple(self._packages)

    @property
    def trucks(self):
        return tuple(self._trucks)

    @property
    def routes(self):
        return tuple(self._routes)

    @property
    def customers(self):
        return tuple(self._customers)

    @property
    def logged_in_user(self):
        return self._logged_in_user

    @logged_in_user.setter
    def logged_in_user(self, value):
        self._logged_in_user = value

    def login_user(self, user_role):
        self._logged_in_user = user_role


    def logout_user(self):
        self.logged_in_user = None

    def create_customer(self, f_name, l_name, email):
        new_customer = Customer(f_name, l_name, email)
        self._customers.append(new_customer)
        return new_customer

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
                        distance = next_city[i][1]
                        time = distance / 87
                        return (distance, time)

    def find_package_by_id(self, pack_id):
        for pack in self._packages:
            if pack._id == pack_id:
                return pack

    def find_free_trucks_by_location(self, location: str):
        trucks = []
        for truck in self._trucks:
            if truck.status == "free" and truck.location == location:
                trucks.append(truck)

        if len(trucks) == 0:
            return None

        return trucks

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

    def get_accepted_packages(self):
        """Трябва да връща пратките със статус accepted"""
        accepted_packages = filter(
            lambda x: x.Package_status == "accepted", self._packages
        )
        return list(accepted_packages)

    def find_customer_by_email(self, mail):
        for person in self._customers:
            if person._email == mail:
                return True
        return False

    def view_routes_in_progress(self):
        """
        Only a manager should be able to perform this task!
        """
        temp_result = []
        for route in self._routes:
            if route.status == Route.IN_PROGRESS:
                temp_result.append(route)

        result_to_return = []
        for r in temp_result:
            result_to_return.append(str(r))

        return "\n".join(result_to_return)

    def view_pending_packages(self):
        found_packages = {}
        for package in self._packages:
            if package.status == Package_status.ACCEPTED:
                if package.start_location not in found_packages:
                    found_packages[package.start_location] = 1
                else:
                    found_packages[package.start_location] += 1

        total_packages = sum(found_packages.values())
        result = [f"Total packages waiting to be assigned: {total_packages}."]

        for location, packages in found_packages.items():
            result.append(f" - {location}: {packages} package/s")

        return "\n".join(result)

    def view_locations(self):
        towns = {
            "Sydney": [],
            "Melbourne": [],
            "Adelaide": [],
            "Alice springs": [],
            "Brisbane": [],
            "Darwin": [],
            "Perth": [],
        }
        for package in self._packages:
            if package.location in Cities.cities:
                towns[package.location].append(package.weight)

        output = []

        for key, value in towns.items():
            output.append(
                f"{key.capitalize()} has packages with total weight {sum(value)}kg."
            )

        return "\n".join(output)

    def view_location(self, location):
        city_packages = []
        for package in self._packages:
            if (
                package.location == location
                and package.status == Package_status.ACCEPTED
            ):
                city_packages.append(package)

        towns = {}

        for package in city_packages:
            if package.end_location not in towns:
                towns[f"{package.end_location}"] = package.weight
                continue
            towns[f"{package.end_location}"] += package.weight

        if not len(towns) == 0:
            for key, value in towns.items():
                output = [f"{location} has packages for these locations:"]
                output.append(f"{key} with total weight {value}kg.")
        else:
            output = [f"No packages in {location}."]

        return "\n".join(output)
