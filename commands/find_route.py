from validation_helpers import validate_params_count
from core.application_data import ApplicationData


class FindRouteCommand:
    def __init__(self, params, app_data) -> None:
        validate_params_count(params, 2)
        self._params = params
        self._app_data = app_data

    def execute(self):
        start_location, delivery_adress = self._params

        route = self._app_data.find_route_by_locations(start_location, delivery_adress)
        # този метод трябва да се напише в app_data.
        # ако намери път, трябва да върне пътя
        # ако не намери път да връща грешка с текс "Няма намерен път от {start_location} до {delivery_adress}"

        return f"{route}"
        # тук връща __STR__ имплементацията на пътя
