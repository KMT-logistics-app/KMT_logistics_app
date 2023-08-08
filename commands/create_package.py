from validation_helpers import validate_params_count
from core.application_data import ApplicationData
from models.package import Package


class CreatePackageCommand:
    def __init__(self, params, app_data) -> None:
        validate_params_count(params, 4)
        self._params = params
        self._app_data = app_data

    def execute(self):

        start_location, delivery_adress, weight, customer_info = self._params
        self._app_data.create_package(start_location, delivery_adress, weight, customer_info)
        # create_package трябва да се напише в application_data и освен, че създава пакета, трябва да го добавя в списъка с пакети
        # в самия Package клас трябв да се сложи counter, който започва от 1, за да може
        #  при създаването на пакети да се инициализира автоматично ID
        # Калоян: weight трябва да опитваме да се парсне към float (14,5кг е валидно тегло) try_parse_float() функция

        return f"Package from {customer_info} was created."
