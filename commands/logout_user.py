from core.application_data import ApplicationData


class LogoutUserCommand:
    def __init__(self, app_data: ApplicationData) -> None:
        self._app_data = app_data

    def execute(self):
        self._app_data.logout_user()

        return f'Log out successful'
