from commands.validation_helpers import (
    validate_params_count,
    ensure_valid_location_name,
)
from core.application_data import ApplicationData


class ViewLocationCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        if self._app_data.logged_in_user == None:
            return 'You have to log in to perform this operation!'
        
        location = ensure_valid_location_name(self._params[0])
        
        return self._app_data.view_location(location)
        