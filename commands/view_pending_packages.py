from commands.validation_helpers import validate_params_count, try_parse_int
from core.application_data import ApplicationData


class ViewPackageCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        package_id = try_parse_int(self._params[0])

        package = self._app_data.find_package_by_id(package_id)

        return str(package)
    
# да го оправя така, че да дава информация за всички пакети (брой намерени пакети, локациите им)