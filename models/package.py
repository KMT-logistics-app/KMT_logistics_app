from models.constants.package_status import Package_status
# from models.customer import Customer
from datetime import datetime


class Package:
    id_counter = 0

    def __init__(self, weight, start_location, end_location, contact_info) -> None:

        self.weight: float = weight
        self._start_location: str = start_location
        self._end_location: str = end_location
        self._contact_info: list = contact_info 
        self._id = self.create_id()
        self.status = Package_status.ACCEPTED
        self._history = []
        self._accepted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._history.append(f'Package accepted on {self._accepted_time}')
         

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

    def time_loaded(self, value):
        self.status = Package_status.LOADED
        self._history.append(f'Package loaded on {value}')
        
    
    def time_delivered(self, value):
        self.status = Package_status.DELIVERED
        self._history.append(f'Package delivered to {self.end_location} on {value}')


    def package_details(self):
        # if self.status == Package_status.ACCEPTED:
        return f"Weight {self.weight}kgs\
            \nAccepted in {self.start_location} at {self._accepted_time}\
            \nStatus: {self.status}"
        # if self.status == Package_status.LOADED:
        #     return f"Weight {self.weight}kgs\
        #         \nLoaded in {self.start_location} at {self.time_loaded}\
        #         \nStatus: {self.status}"
        

    def __str__(self) -> str:

        return f"Package: #{self._id}\nETA: tomorrow :)\nDetails: {self.package_details()}"
        
        


# класа трябва да има __str__ имплементация, защото ще се използва по-горе

# - ID
# - weight(kg)
# - start location
# - end location
# - contact information for the customer
# - assigned status
# expected delivery time -> to be implemented
