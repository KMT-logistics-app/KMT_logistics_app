from commands.validation_helpers import validate_params_count

from core.application_data import ApplicationData


class FindFreeTrucksByLocationCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        location = self._params[0]
        trucks = self._app_data.find_free_trucks_by_location(location)

        if trucks == None:
            return f"No free trucks at {location}"

        output = []
        for truck in trucks:
            output.append(str(truck))

        return "\n".join(output)
