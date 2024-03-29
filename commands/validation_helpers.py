from models.constants.cities import Cities
from models.constants.roles import Roles

def create_customer_info(info: str):
    try:
        contact_info = info.split('-')
        first_name, last_name = contact_info[0].split('_')
        email = contact_info[1]
        return first_name, last_name, email
    except IndexError:
        raise IndexError('Incorrectly formatted contact info')

def ensure_valid_location_name(location_name: str):
    if location_name.capitalize() in Cities.cities:
        return location_name.capitalize()
    raise NameError(f"{location_name} is not a valid city.")

def try_parse_float(value):
    try:
        value = float(value)
        return value
    except ValueError as e:
        raise e


def try_parse_int(value):
    try:
        value = int(value)
        return value
    except ValueError as e:
        raise e

def validate_params_count(params, count):
    if len(params) != count:
        raise ValueError(
            f'Invalid number of arguments. Expected: {count}; received: {len(params)}.")'
        )

def validate_user_role(role: str):
    roles = [Roles.EMPLOYEE, Roles.MANAGER, Roles.SUPERVISOR]
    if role.lower() not in roles:
        raise ValueError('Invalid user role!')
    return role.lower()