from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count


class LoginUserCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        # login, Manager
        log_user = self._params[0]
        user = self._app_data.login_user(log_user)
        if user is None:
            return f"Have Logged User"

        return f"Login successful {user}"

