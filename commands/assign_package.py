from validation_helpers import validate_params_count
from core.application_data import ApplicationData


class AssignPackageCommand:
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 2)
        self._params = params
        self._app_data = app_data

    def execute(self):
        package_id = self._params[0]
        truck_id = self._params[-1]

        package = self._app_data.find_package_by_id(package_id)
        truck = self._app_data.find_truck_by_id(truck_id)

        truck.assign_package(package)
        # да се добави функцията в truck и да се наследи от всеки камион

        return f"Package {package_id} assigned to truck {truck_id}"
