import unittest
from core.application_data import ApplicationData
from commands.create_route import CreateRouteCommand
from models.truck import Truck
from datetime import datetime
from models.customer import Customer

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

    def test_free_intervals_ReturnsProperly(self):
        truck = APP_DATA.create_truck()
        route_points = ("Sydney", "Melbourne")
        departure_time = datetime(year=2023, month=8, day=21, hour=6, minute=00)
        route = APP_DATA.create_route(route_points, departure_time)
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
        route_points = ("Sydney", "Melbourne")
        departure_time = datetime(2023, 8, 21, 6, 00)
        route = APP_DATA.create_route(route_points, departure_time)
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
        route_points = ("Sydney", "Melbourne")
        departure_time = datetime(2023, 8, 21, 6, 00)
        route = APP_DATA.create_route(route_points, departure_time)

        self.assertEqual(
            (1, VALID_ROUTE_STATUS_PENDING, ("Sydney", "Melbourne"), 877, None, []),
            (
                route.ROUTE_ID,
                route.status,
                route.route_points,
                route.distance,
                route.truck,
                route._packages,
            ),
        )

    def test_assign_package_AssignsPackageProperly(self):
        route_points = ("Sydney", "Melbourne")
        departure_time = datetime(2023, 8, 21, 6, 00)
        route = APP_DATA.create_route(route_points, departure_time)
        customer = Customer("Petar", "Ivanov", "pepi@mail.bg")
        package = APP_DATA.create_package("Sydney", "Melbourne", 500, customer)
        route.assign_package(package)

        self.assertEqual(package, route.packages[0])
