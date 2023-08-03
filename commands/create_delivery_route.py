# from validation_helpers import validate_params_count
# from core.application_data import ApplicationData


# class CreateDeliveryRouteCommand:
#     def __init__(self, params, app_data: ApplicationData) -> None:
#         validate_params_count(params, 1)
#         self._params = params
#         self._app_data = app_data

#     def execute(self):
#         destinations = self._params.split("-")

#         starting_point = destinations[0].lower()
