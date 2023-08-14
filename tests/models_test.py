import unittest
from core.application_data import ApplicationData
from models.truck import Truck
from datetime import datetime
from models.customer import Customer
from models.package import Package
from models.constants.package_status import Package_status

VALID_TRUCK_STATUS_FREE = "free"
VALID_TRUCK_STATUS_BUSY = "busy"

VALID_TRUCK_BRAND_MAN = "Man"
VALID_TRUCK_BRAND_SCANIA = "Scania"
VALID_TRUCK_BRAND_ACTROSS = "Actross"

VALID_CAPACITY_SCANIA = 42000
VALID_CAPACITY_MAN = 37000
VALID_CAPACITY_ACTROSS = 26000
VALID_MAX_RANGE_SCANIA = 8000
VALID_MAX_RANGE_MAN = 10000
VALID_MAX_RANGE_ACTROSS = 13000

VALID_TRUCK_FIRST_LOCATION = "Sydney"
APP_DATA = ApplicationData()

VALID_ROUTE_STATUS_IN_PROGRESS = "in progress"
VALID_ROUTE_STATUS_PENDING = "pending"
VALID_ROUTE_STATUS_FINISHED = "finished"

VALID_ROUTE_POINTS = ("Sydney", "Melbourne")
VALID_DEPARTURE_TIME = datetime(2023, 8, 21, 6, 00)
VALID_CUSTOMER = Customer("Petar", "Ivanov", "pepi@mail.bg")
VALID_PACKAGE_ONE = APP_DATA.create_package("Sydney", "Melbourne", 500, VALID_CUSTOMER)
VALID_PACKAGE_TWO = APP_DATA.create_package("Sydney", "Melbourne", 800, VALID_CUSTOMER)


class Truck_Should(unittest.TestCase):
    def test_initializer_AssignsValuesProperly(self):
        trucks = [Truck]
        for _ in range(40):
            truck = APP_DATA.create_truck()
            trucks.append(truck)
            if 1001 <= truck.TRUCK_ID <= 1010:
                self.assertEqual(
                    (
                        truck.brand,
                        truck.capacity,
                        truck.range,
                        truck.status,
                        truck.location,
                    ),
                    (
                        VALID_TRUCK_BRAND_SCANIA,
                        VALID_CAPACITY_SCANIA,
                        VALID_MAX_RANGE_SCANIA,
                        VALID_TRUCK_STATUS_FREE,
                        VALID_TRUCK_FIRST_LOCATION,
                    ),
                )
            elif 1011 <= truck.TRUCK_ID <= 1025:
                self.assertEqual(
                    (
                        truck.brand,
                        truck.capacity,
                        truck.range,
                        truck.status,
                        truck.location,
                    ),
                    (
                        VALID_TRUCK_BRAND_MAN,
                        VALID_CAPACITY_MAN,
                        VALID_MAX_RANGE_MAN,
                        VALID_TRUCK_STATUS_FREE,
                        VALID_TRUCK_FIRST_LOCATION,
                    ),
                )
            elif 1026 <= truck.TRUCK_ID <= 1040:
                self.assertEqual(
                    (
                        truck.brand,
                        truck.capacity,
                        truck.range,
                        truck.status,
                        truck.location,
                    ),
                    (
                        VALID_TRUCK_BRAND_ACTROSS,
                        VALID_CAPACITY_ACTROSS,
                        VALID_MAX_RANGE_ACTROSS,
                        VALID_TRUCK_STATUS_FREE,
                        VALID_TRUCK_FIRST_LOCATION,
                    ),
                )

    def test_free_intervals_ReturnsProperly(
        self,
    ):  # this is test for Route.assign_truck and Route.calculate_estimated_time commands
        truck = APP_DATA.create_truck()
        route = APP_DATA.create_route(VALID_ROUTE_POINTS, VALID_DEPARTURE_TIME)
        route.assign_truck(truck)
        truck._routes.append(route)

        self.assertEqual(
            [
                [datetime.min, route.departure_time],
                [route.calculate_estimated_time(), datetime.max],
            ],
            truck.free_intervals,
        )

    def test_str_method_ReturnsProperly(self):
        truck = APP_DATA.create_truck()
        route = APP_DATA.create_route(VALID_ROUTE_POINTS, VALID_DEPARTURE_TIME)
        route.assign_truck(truck)
        truck._routes.append(route)
        availability = ""
        for interval in truck.free_intervals:
            availability += f"From {interval[0]} to {interval[1]}\n"

        self.assertEqual(
            f"Truck ID: {truck.truck_id}.\
            \n  Location: {truck.location}.\
            \n  Brand: {truck.brand}.\
            \n  Capacity: {truck.capacity}kg.\
            \n  Range: {truck.range}km.\
            \n  Status: {truck.status}.\
            \n  Availability: \n{availability.strip()}",
            str(truck),
        )


class Route_Should(unittest.TestCase):
    def test_initializer_AssignsValuesProperly(self):
        route = APP_DATA.create_route(VALID_ROUTE_POINTS, VALID_DEPARTURE_TIME)

        self.assertEqual(
            (2, VALID_ROUTE_STATUS_PENDING, ("Sydney", "Melbourne"), 877, None, []),
            (
                route.route_id,
                route.status,
                route.route_points,
                route.distance,
                route.truck,
                route._packages,
            ),
        )

    def test_assign_package_AssignsPackageProperly(self):
        route = APP_DATA.create_route(VALID_ROUTE_POINTS, VALID_DEPARTURE_TIME)
        route.assign_package(VALID_PACKAGE_ONE)

        self.assertEqual(VALID_PACKAGE_ONE, route.packages[0])

    def test_truck_capacity_and_packages_weight_CalculateProperly(self):
        route = APP_DATA.create_route(VALID_ROUTE_POINTS, VALID_DEPARTURE_TIME)
        truck = APP_DATA.create_truck()
        route.assign_package(VALID_PACKAGE_ONE)
        route.assign_package(VALID_PACKAGE_TWO)
        route.assign_truck(truck)

        self.assertEqual(
            truck.capacity - VALID_PACKAGE_ONE.weight - VALID_PACKAGE_TWO.weight,
            route.truck_capacity(),
        )

    def test_str_ReturnsCorrectString(self):
        route = APP_DATA.create_route(VALID_ROUTE_POINTS, VALID_DEPARTURE_TIME)
        truck = APP_DATA.create_truck()
        route.assign_package(VALID_PACKAGE_ONE)
        route.assign_truck(truck)
        self.assertEqual(
            f'Route ID: {route._id}\
        \n  Status: {route.status}\
        \n  Total distance: {route._distance}km\
        \n  Route details: {" -> ".join(route.route_points)}\
        \n  Packages: {len(route._packages)} with total weight {route.packages_weight()}kgs\
        \n  Truck assigned: \n{str(route.truck) if route.truck else None}',
            str(route),
        )


class Package_Should(unittest.TestCase):
    def test_initializer_AssignsValuesCorrectly(self):
        package = Package("Sydney", "Darwin", 1000, VALID_CUSTOMER)

        self.assertEqual(
            ("Sydney", "Darwin", 1000, VALID_CUSTOMER.first_name, None, None, Package_status.ACCEPTED),
            (
                package.start_location,
                package.end_location,
                package.weight,
                package._contact_info.first_name,
                package.estimated_arrival_time,
                package.route,
                package.status
            ),
        )
