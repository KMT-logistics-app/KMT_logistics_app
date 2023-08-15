from commands.validation_helpers import validate_params_count, try_parse_int
from core.application_data import ApplicationData
from models.constants.package_status import Package_status


class AssignPackageCommand:
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 2)
        self._params = params
        self._app_data = app_data

    def execute(self):
        if self._app_data.logged_in_user == None:
            return 'You have to log in to perform this operation!'
                
        package_id = try_parse_int(self._params[0])
        route_id = try_parse_int(self._params[-1])

        package = self._app_data.find_package_by_id(package_id)
        route = self._app_data.find_route_by_id(route_id)
        
        if package._status == Package_status.ASSIGNED:
            return f'Package {package_id} already assigned.'

        if route.truck_capacity() >= package.weight:
            route.assign_package(package)
            package.route = route
            return f"Package {package_id} was assigned to route {route_id}."
        else:
            return f"The truck in route {route_id} don't have capacity for this package. You have to create another route."
