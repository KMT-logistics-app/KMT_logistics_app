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
        if self._app_data.logged_in_user == None:
            return 'You have to log in to perform this operation!'

        start_location, delivery_location = self._params
        
        start_location = ensure_valid_location_name(start_location)
        delivery_location = ensure_valid_location_name(delivery_location)
        route = self._app_data.find_route_by_locations(start_location, delivery_location)

        if route:
            result = [f'Found {len(route)} routes:']
            result2 = [str(rt) for rt in route]
            result.extend(result2)
            return '\n'.join(result)
        else:
            return "No suitable route found."
