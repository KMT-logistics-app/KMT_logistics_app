from core.application_data import ApplicationData


class CreateTruckCommand:
    def __init__(self, app_data: ApplicationData) -> None:
        self._app_data = app_data

    def execute(self):
        new_truck = self._app_data.create_truck()

        return f"Truck {new_truck.brand} with ID {new_truck._truck_id}was created."
