from core.application_data import ApplicationData
from models.constants.package_status import Package_status


class ViewPendingPackagesCommand:
    def __init__(self, app_data: ApplicationData) -> None:
        self._app_data = app_data

    def execute(self):

        user = self._app_data.logged_in_user
        if user == 'Employee':
            return f"You don't have permission"
        else:
            found_packages = {}
            for package in self._app_data._packages:
                if package.status == Package_status.ACCEPTED:
                    if package.start_location not in found_packages:
                        found_packages[package.start_location] = 1
                    else:
                        found_packages[package.start_location] += 1

            total_packages = sum(found_packages.values())
            result = [f'Total packages waiting to be assigned: {total_packages}.']

            for location, packages in found_packages.items():
                result.append(f' - {location}: {packages} packages')

            return '\n'.join(result)

    # found_packages = {}
    # for package in self._app_data._packages:
    #         if package.status == Package_status.ACCEPTED:
    #             if package.start_location not in found_packages:
    #                 found_packages[package.start_location] = 1
    #             else:
    #                 found_packages[package.start_location] += 1
    #
    #     total_packages = sum(found_packages.values())
    #     result = [f'Total packages waiting to be assigned: {total_packages}.']
    #
    #     for location, packages in found_packages.items():
    #         result.append(f' - {location}: {packages} packages')
    #
    #     return '\n'.join(result)

# да го оправя така, че да дава информация за всички пакети (брой намерени пакети, локациите им)
