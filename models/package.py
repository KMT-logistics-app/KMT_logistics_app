from models.constants.package_status import Package_status
from models.constants.cities import Cities
from models.customer import Customer
from datetime import datetime, timedelta


class Package:
    id_counter = 0

    def __init__(self, start_location, end_location, weight, contact_info) -> None:
        self.weight: float = weight
        self._start_location: str = start_location
        self._end_location: str = end_location
        self._contact_info = contact_info  # to be modified
        self.route = None
        self._id = self.create_id()
        self.status = Package_status.ACCEPTED
        self._accepted_time = datetime.now()
        self._delivery_time_needed = self.time_needed()
        self.estimated_arrival_time = None

    @property
    def location(self):
        if self.route == None or self.route.departure_time < datetime.now():
            return self._start_location

    @property
    def status(self):
        if self.estimated_arrival_time == None:
            return Package_status.ACCEPTED
        if self.route != None and datetime.now() > self.estimated_arrival_time:
            return Package_status.DELIVERED
        if self.route != None and datetime.now() < self.route.departure_time:
            return Package_status.ASSIGNED
        return Package_status.LOADED

    @property
    def delivery_time_needed(self):
        return self._delivery_time_needed

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Package should weigh more than 0.0kgs")

        self._weight = value

    @property
    def start_location(self):
        return self._start_location

    @property
    def end_location(self):
        return self._end_location

    def create_id(self):
        Package.id_counter += 1
        return Package.id_counter

    def time_loaded(self):  # да обсъдим дали има смисъл от този метод
        self.status = Package_status.LOADED
        return datetime.today()

    def time_needed(self):
        for current, next_city in Cities.DISTANCES.items():
            if current == self._start_location:
                for i in range(len(next_city)):
                    if self._end_location == next_city[i][0]:
                        return timedelta(hours=next_city[i][1] / 87)

    def package_details(self):
        return f"Weight {self.weight}kgs\nAccepted in {self.start_location} at {self._accepted_time}\nStatus: {self.status}"

    def __str__(self) -> str:
        return f"Package: #{self._id}\nExpected delivery time: {self.estimated_arrival_time}.\nDetails: {self.package_details()}"


# класа трябва да има __str__ имплементация, защото ще се използва по-горе

# - ID
# - weight(kg)
# - start location
# - end location
# - contact information for the customer
# - assigned status
# - expected delivery time
