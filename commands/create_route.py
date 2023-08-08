from commands.validation_helpers import ensure_valid_location_name
from core.application_data import ApplicationData
from datetime import datetime


class CreateRouteCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        if len(params) < 3:
            raise ValueError("Please enter at least two route points.")
        self._params = params
        self._app_data = app_data

        # createroute Alice Springs Adelaide Melbourne Sydney Brisbane 2023/10/03/12/00

    def execute(self):
        route_points = self._params[:-1]
        for point in route_points:
            ensure_valid_location_name(point)
        departure_time = self._params[-1]
        year, month, day, hour, minutes = departure_time.split("/")
        parsed_departure = datetime(
            int(year), int(month), int(day), int(hour), int(minutes)
        )
        new_route = self._app_data.create_route(route_points, parsed_departure)
        # метода трябва да се разпише в app_data, kaто този метод
        # трябва да създава Route(start_point, delivery_adress) самия клас Route трябва да генерира уникално ID
        # и да включва час тръгване и час пристигане
        return f"Delivery route {new_route._id} was created."
