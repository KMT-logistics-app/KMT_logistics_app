from employee import Employee
from constants.roles import Roles
from core.application_data import ApplicationData


class Supervisor(Employee):
    def __init__(self, _role) -> None:
        Employee.__init__()

        self._role = Roles.MANAGER


    def view_accept_pack(self):
        return self._appdata.get_accepted_packages()
