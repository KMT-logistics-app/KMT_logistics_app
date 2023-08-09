from commands.validation_helpers import (
    validate_params_count,
    ensure_valid_location_name,
)
from core.application_data import ApplicationData


class FindRouteCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 2)
        self._params = params
        self._app_data = app_data

    def execute(self):
        start_location, delivery_adress = self._params
        ensure_valid_location_name(start_location)
        ensure_valid_location_name(delivery_adress)
        route = self._app_data.find_route_by_locations(start_location, delivery_adress)

        if route:
            return "\n".join(route)
        else:
            return "There is no suitable root."
