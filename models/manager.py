from models.constants.roles import Roles
from models.employee import Employee


class Manager(Employee):
    def __init__(self) -> None:
        Employee.__init__()

        self._role = Roles.MANAGER

    @property
    def role(self):
        return self._role
