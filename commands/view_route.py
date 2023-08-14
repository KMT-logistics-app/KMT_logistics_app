from commands.validation_helpers import validate_params_count, try_parse_int
from core.application_data import ApplicationData


class ViewRouteCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        route_id = try_parse_int(self._params[0])

        route = self._app_data.find_route_by_id(route_id)

        return str(route) if route != None else f'Route {route_id} not found'
