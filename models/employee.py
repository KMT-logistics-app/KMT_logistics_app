from models.constants.roles import Roles


class Employee:
    def __init__(self) -> None:
        self._role = Roles.EMPLOYEE

    @property
    def role(self):
        return self._role
