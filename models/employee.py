from constants.roles import Roles
from models.customer import Customer
from models.package import Package
from models.route import Route

class Employee:

    # can:
    # create a package
    # create a route 
    # search for a route, based on the start and end locations
    # assign a free truck to a route
    # assign a package to a truck
    # view route
    # view truck
    # view package

    # has:
    # role - worker, manager, supervisor

    def __init__(self) -> None:
        self._role = Roles.WORKER


    @property
    def role(self):
        return self._role


    def create_package(self, weight, start, end, customer: Customer):
        return Package(weight, start, end, customer)


    def create_route(self, lst):
        return Route(lst)


    def find_route(self):
        # in Application data?
        pass


    def assign_truck_to_route(self):
        # in Application data?
        pass


    def assign_package_to_truck(self):
        # in Application data?
        pass


    def view_route(self, start, end):
        # in Application data?
        pass


    def view_truck(self, truck_id):
        # in Application data?
        pass


    def view_package(self, package_id):
        # in Application data?
        pass

