from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, validate_user_role


class LoginUserCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 1)
        self._params = params[0]
        self._app_data = app_data

    def execute(self):
        user_to_log = validate_user_role(self._params)

        if self._app_data.logged_in_user != None:
            return f'The current user has to log out first!'
        else:
            self._app_data.login_user(user_to_log)

        return f"{user_to_log.capitalize()} logged in successfully."

