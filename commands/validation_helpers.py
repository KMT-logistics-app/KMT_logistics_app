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