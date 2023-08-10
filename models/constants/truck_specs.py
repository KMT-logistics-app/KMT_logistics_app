class TruckStatus:
    FREE = "free"
    BUSY = "busy"


class TruckBrand:
    MAN = "Man"
    SCANIA = "Scania"
    ACTROSS = "Actross"
    truck_brands = [ACTROSS, MAN, SCANIA]


class TruckSpecs:
    CAPACITY_SCANIA = 42000
    MAX_RANGE_SCANIA = 8000

    CAPACITY_MAN = 37000
    MAX_RANGE_MAN = 10000

    CAPACITY_ACTROSS = 26000
    MAX_RANGE_ACTROSS = 13000
