from commands.validation_helpers import validate_params_count
from core.application_data import ApplicationData


class LogoutUserCommand:
    def __init__(self, app_data: ApplicationData) -> None:
        self._app_data = app_data

    # logout
    def execute(self):
        self._app_data.logout_user()
        return f'user is now logged out'
