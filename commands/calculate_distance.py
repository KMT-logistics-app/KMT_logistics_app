from commands.validation_helpers import validate_params_count, ensure_valid_location_name
from core.application_data import ApplicationData


class CalculateDistanceCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 2)
        self._params = params
        self._app_data = app_data


    def execute(self):

        point_A, point_B = self._params
        ensure_valid_location_name(point_A)
        ensure_valid_location_name(point_B)

        return self._app_data.calculate_distance(point_A, point_B)