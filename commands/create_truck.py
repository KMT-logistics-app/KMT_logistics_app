from validation_helpers import validate_params_count
from core.application_data import ApplicationData


class CreateTruckCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        truck_id = self._params[0]
        new_truck = self._app_data.create_truck(truck_id)

        return f"Truck {new_truck.brand} was created."
