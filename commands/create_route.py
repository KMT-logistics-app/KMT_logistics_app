from validation_helpers import validate_params_count
from core.application_data import ApplicationData


class CreateRouteCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 2)
        self._params = params
        self._app_data = app_data

    def execute(self):
        starting_point, delivery_adress = self._params

        self._app_data.create_route(starting_point, delivery_adress)
        # метода трябва да се разпише в app_data, kaто този метод
        # трябва да създава Route(start_point, delivery_adress) самия клас Route трябва да генерира уникално ID
        # и да включва час тръгване и час пристигане
        return f"Delivery route from {starting_point} to {delivery_adress} was created."
