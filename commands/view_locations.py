from core.application_data import ApplicationData


class ViewLocationsCommand:
    def __init__(self, app_data: ApplicationData):
        self._app_data = app_data

    def execute(self):
        if self._app_data.logged_in_user != 'manager':
            return 'Access denied! Only a manager can perform this operation!'
        else:
            output = self._app_data.view_locations()

        return output
