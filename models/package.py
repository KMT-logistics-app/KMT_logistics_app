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
        self._contact_info = contact_info # to be modified
        self._id = self.create_id()
        self.status = Package_status.ACCEPTED
        self._accepted_time = datetime.now().strftime('%Y/%m/%d %H:%M')
        self._time_loaded = self.time_loaded()
        self._expected_delivery_time = self.est_delivery_time()

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

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def create_id(self):
        Package.id_counter += 1
        return Package.id_counter

    def time_loaded(self): # да обсъдим дали има смисъл от този метод
        self.status = Package_status.LOADED
        return datetime.today()

    def est_delivery_time(self):
        for current, next_city in Cities.DISTANCES.items():
            if current == self._start_location:
                for i in range(len(next_city)):
                    if self._end_location == next_city[i][0]:
                        return self._accepted_time + str(timedelta(hours=next_city[i][1] / 87).days)

    def package_details(self):
        return f"Weight {self.weight}kgs\nAccepted in {self.start_location} at {self._accepted_time}\nStatus: {self.status}"

    def __str__(self) -> str:
        return f"Package: #{self._id}\nExpected delivery time: {self._expected_delivery_time}.\nDetails: {self.package_details()}"


# класа трябва да има __str__ имплементация, защото ще се използва по-горе

# - ID
# - weight(kg)
# - start location
# - end location
# - contact information for the customer
# - assigned status
# - expected delivery time 
