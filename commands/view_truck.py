from commands.validation_helpers import validate_params_count, try_parse_int
from core.application_data import ApplicationData


class ViewTruckCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        truck_id = try_parse_int(self._params[0])

        truck = self._app_data.find_truck_by_id(truck_id)

        return str(truck) if truck != None else f'Truck with ID {truck_id} doesn\'t exist.'
