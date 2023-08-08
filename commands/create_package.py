from commands.validation_helpers import validate_params_count, try_parse_float
from core.application_data import ApplicationData
from models.package import Package


class CreatePackageCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 4)
        self._params = params
        self._app_data = app_data

        # createpackage sydney Melbourne 50 ivan_ivanov_ivan@mail.bg

    def execute(self):

        start_location, delivery_adress, weight, contact_info = self._params
        start_location = self.ensure_valid_location_name(start_location)
        delivery_adress = self.ensure_valid_location_name(delivery_adress)
        weight = try_parse_float(weight)
        self._app_data.create_package(start_location, delivery_adress, weight, contact_info)
        # create_package трябва да се напише в application_data и освен, че създава пакета, трябва да го добавя в списъка с пакети
        # в самия Package клас трябв да се сложи counter, който започва от 1, за да може
        #  при създаването на пакети да се инициализира автоматично ID
        # Калоян: weight трябва да опитваме да се парсне към float (14,5кг е валидно тегло) try_parse_float() функция

        return f"Package from {contact_info} was created."


    def ensure_valid_location_name(self, location_name: str):
        
        return location_name.capitalize()