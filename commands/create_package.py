from commands.validation_helpers import (
    validate_params_count,
    try_parse_float,
    ensure_valid_location_name,
    create_customer_info

)
from core.application_data import ApplicationData
from models.customer import Customer


class CreatePackageCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        validate_params_count(params, 4)
        self._params = params
        self._app_data = app_data
        
        # createpackage, Alice Springs, Adelaide, 500, Ivan_Ivanov-ivan@mail.au
        # createpackage, Adelaide, Sydney, 500.3, Ivan_Ivanov-ivan@mail.au

    def execute(self):
        # package info
        start_location, delivery_adress, weight, contact_info = self._params
        start_location = ensure_valid_location_name(start_location)
        delivery_adress = ensure_valid_location_name(delivery_adress)
        weight = try_parse_float(weight)
        # customer info
        first_name, last_name, email = create_customer_info(contact_info) 
        customer = Customer(first_name, last_name, email)
        # if customer is created properly, we can create the package
        package = self._app_data.create_package(
            start_location, delivery_adress, weight, customer
        )
        # add the customer to the app_data customers list and add the package to the customer
        if not self._app_data.find_customer_by_email(email):
            self._app_data._customers.append(customer)
            customer.add_package(package)
        else:
            customer.add_package(package)
        
        return f"Package from {first_name} {last_name} was accepted."

