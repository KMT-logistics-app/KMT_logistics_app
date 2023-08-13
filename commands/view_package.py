from commands.validation_helpers import validate_params_count, try_parse_int
from core.application_data import ApplicationData
from models.customer import Customer


class ViewPackageCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        package_id = try_parse_int(self._params[0])

        package = self._app_data.find_package_by_id(package_id)

        if not package == None:
            return self.leave_feedback(package)
        
        return self.leave_feedback(f'Sorry, package {package_id} not found.')


    def leave_feedback(self, result):
        if isinstance(result, str):
            return f'{result}\
                    \n***Customer left negative feedback:\
                    \n  "What??? You lost my package along the way?!\
                    \n  I won\'t use your services any more!"'
        else:
            first_name = result._contact_info.first_name
            last_name = result._contact_info.last_name
            return f'{str(result)}\
                    \n***Customer {first_name} {last_name} feedback:\
                    \n  "Thank you very much! You are the best logistics company :)"'
    