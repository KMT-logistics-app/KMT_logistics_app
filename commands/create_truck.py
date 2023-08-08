from core.application_data import ApplicationData


class CreateTruckCommand:
    def __init__(self, app_data: ApplicationData) -> None:
        # validate_params_count(params)
        # self._params = params  # init-а на truck не приема параметри
        self._app_data = app_data

    def execute(self):
        # truck_id = self._params[0] # id се генерира при инстанцирането на truck
        new_truck = self._app_data.create_truck()

        return f"Truck {new_truck.brand} was created."
