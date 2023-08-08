from models.constants.cities import Cities


def validate_params_count(params, count):
    if len(params) != count:
        raise ValueError(
            f'Invalid number of arguments. Expected: {count}; received: {len(params)}.")'
        )


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


def ensure_valid_location_name(location_name):
    if location_name.capitalize() in Cities.cities:
        return location_name.capitalize()
    raise NameError(f"{location_name} is not a valid city.")
