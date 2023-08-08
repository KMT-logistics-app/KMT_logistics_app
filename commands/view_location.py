from commands.validation_helpers import (
    validate_params_count,
    ensure_valid_location_name,
)
from core.application_data import ApplicationData


class ViewTownCommand:
    def __init__(self, params, app_data) -> None:
        validate_params_count(1, params)
        self._params = params
        self._app_data = app_data

    def execute(self):
        town = ensure_valid_location_name(self._params[0])
