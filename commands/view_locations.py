from core.application_data import ApplicationData


class ViewAllPackagesCommand:
    def __init__(self, app_data: ApplicationData):
        self._app_data = app_data

    def execute(self):
        output = self._app_data.view_all_packages()

        return f"{output}"
