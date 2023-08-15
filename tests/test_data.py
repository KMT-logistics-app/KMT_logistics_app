# the place for the common values we'll use for many tests

# route(start_location, mid_location, end_location, datetime_object)

VALID_DATE = '2024/06/12/09/00'
VALID_START_LOCATION = 'Sydney'
VALID_MID_LOCATION = 'Adelaide'
VALID_END_LOCATION = 'Melbourne'
VALID_ROUTE = f'{VALID_START_LOCATION}, {VALID_END_LOCATION}, {VALID_DATE}'

INVALID_ROUTE = f'{VALID_START_LOCATION}, {VALID_DATE}'
INVALID_LOCATION_NAME = 'Sofia'

# package(start_location, end_location, weight, contact_info)

VALID_WEIGHT = 500
VALID_CONTACT_INFO = 'Ivan_Ivanov-ivan@mail.au'
VALID_PACKAGE = f'{VALID_START_LOCATION}, {VALID_END_LOCATION}, {VALID_WEIGHT}, {VALID_CONTACT_INFO}'

INVALID_PACKAGE = f'{VALID_START_LOCATION}, {INVALID_LOCATION_NAME}, {VALID_WEIGHT}, {VALID_CONTACT_INFO}'
INVALID_CONTACT_INFO = 'Ivan_Ivanov,ivan@mail.au'
