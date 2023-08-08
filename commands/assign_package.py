from commands.validation_helpers import validate_params_count, try_parse_int
from core.application_data import ApplicationData


class AssignPackageCommand:
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 2)
        self._params = params
        self._app_data = app_data

    def execute(self):
        package_id = try_parse_int(self._params[0])
        route_id = try_parse_int(self._params[-1])

        package = self._app_data.find_package_by_id(package_id)
        route = self._app_data.find_route_by_id(route_id)
        # двете функции трябва да се добавят в app_data
        # трябва да връщат обект от съответните класове(package, route) и да връща грешка, ако не намира такива

        if route.trucks_capacity() >= package.weight:
            route.assign_package(package)
            return f"Route {route_id} assigned package {package_id}."
        else:
            return f"Truck's in route {route_id} don't have capacity for this package. You have to assign another vehicle."
