from employee import Employee
from constants.roles import Roles


class Supervisor(Employee):
    def __init__(self) -> None:
        Employee.__init__()

        self._role = Roles.SUPERVISOR

    @property
    def role(self):
        return self._role
