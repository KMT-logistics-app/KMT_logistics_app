from commands.validation_helpers import validate_params_count
from core.application_data import ApplicationData


class AssignTruckCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 4)
        self._params = params
        self._app_data = app_data

    def execute(self):
        truck_id = self._params[0]
        route_id = self._params[-1]

        truck = self._app_data.find_truck_by_id(truck_id)
        route = self._app_data.find_route_by_id(route_id)

        route.assign_truck(truck)
        # трябва да се напише като функция в route

        return f"Truck {truck_id} assigned to route {route_id}"
