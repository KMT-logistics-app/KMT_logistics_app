from employee import Employee
from core.application_data import ApplicationData
from constants.roles import Roles


class Manager(Employee):
    def __init__(self, _role) -> None:
        Employee.__init__()

        self._role = Roles.MANAGER

    def get_routes_in_progress(self):
        return self._appdata.view_routes_in_progress()




# A manager at the company uses the system to find information about all delivery routes in progress
