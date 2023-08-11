from models.constants.truck_specs import TruckBrand, TruckStatus, TruckSpecs
from datetime import datetime


class Truck:
    TRUCK_ID = 1000

    def __init__(self):
        self._truck_id = self.create_id()
        self._brand = self.validate_brand(self._truck_id)
        self._status = TruckStatus.FREE
        self._routes: list = []
        self._capacity = self.validate_capacity()
        self._range = self.validate_range()

    @property
    def location(self):
        if len(self._routes) == 0:
            return "Sydney"
        if self.status == "free":
            for index in range(len(self._routes)):
                if (
                    self._routes[index].calculate_estimated_time() <= datetime.now()
                    and self._routes[index + 1].departure_time > datetime.now()
                ):
                    return self._routes[index].route_points.split(" -> ")[-1]
        return "On the road"

    @property
    def status(self):
        for intervals in self.free_intervals:
            if intervals[0] <= datetime.now() <= intervals[1]:
                return TruckStatus.FREE

        return TruckStatus.BUSY

    @property
    def free_intervals(self):
        courses = len(self._routes)
        if courses == 0:
            return [[datetime.min, datetime.max]]
        if courses == 1:
            return [
                [datetime.min, self._routes[0].departure_time],
                [self._routes[0].calculate_estimated_time(), datetime.max],
            ]

        intervals = []

        for course in range(courses):
            if course == 0:
                intervals.append([datetime.min, self._routes[course].departure_time])
                continue
            intervals.append(
                [
                    self._routes[course - 1].calculate_estimated_time(),
                    self._routes[course].departure_time,
                ]
            )
            if course == courses - 1:
                intervals.append(
                    [self._routes[course].calculate_estimated_time(), datetime.max]
                )

        return intervals

    @property
    def brand(self):
        return self._brand

    @property
    def truck_id(self):
        return self._truck_id

    @property
    def capacity(self):
        return self._capacity

    @property
    def range(self):
        return self._range
    
    @property
    def routes(self):
        return tuple(self._routes)

    def create_id(self):
        Truck.TRUCK_ID += 1
        return Truck.TRUCK_ID

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
        availability = ""
        for interval in self.free_intervals:
            availability += f"From {interval[0]} to {interval[1]}\n"

        return f"Id: {self.truck_id}\nLocation: {self.location}\nBrand: {self.brand}\nCapacity: {self._capacity}\nRange: {self._range}\nStatus: {self.status}\nAvailability: \n{availability.strip()}"
