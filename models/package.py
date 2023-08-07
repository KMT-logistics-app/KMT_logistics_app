from models.constants.packages import Package_status
from models.customer import Customer
from datetime import datetime

class Package:
    id_counter = 0
    def __init__(self, weight, start_location, end_location, contact_info: Customer) -> None:
        self.weight: float = weight
        self._start_location: str = start_location
        self._end_location: str = end_location
        self._contact_info: Customer = str(contact_info)
        self._id = self.create_id()
        self.status = Package_status.ACCEPTED
        self._accepted_time = datetime.now()
        self._time_loaded = self.time_loaded()
        self._delivered_time = self.time_delivered()


    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError('Package should weigh more than 0.0kgs')
        
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


    def time_loaded(self, value):
        self.status = Package_status.IN_PROGRESS
        self._time_loaded = value


    def time_delivered(self, value):
        self.status = Package_status.DELIVERED
        self._delivered_time = value


    def package_details(self):
        return f'Weight {self.weight}kgs\nAccepted in {self.start_location} at {self._accepted_time}\nStatus: {self.status}'


    def __str__(self) -> str:
        if self.status == Package_status.ACCEPTED:
            return f'Package: #{self._id}\nETA: tomorrow :)\nDetails: {self.package_details()}'

# класа трябва да има __str__ имплементация, защото ще се използва по-горе

# - ID
# - weight(kg)
# - start location
# - end location
# - contact information for the customer
# - assigned status
# expected delivery time -> to be implemented