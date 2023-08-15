from core.application_data import ApplicationData


class ViewPendingPackagesCommand:
    def __init__(self, app_data: ApplicationData) -> None:
        self._app_data = app_data

    def execute(self):
        if self._app_data.logged_in_user == 'employee':
            return f"You don't have permission to perform this operation!"
        else:
            pending_packs = self._app_data.view_pending_packages()
            return pending_packs
