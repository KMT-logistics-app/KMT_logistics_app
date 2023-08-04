class TruckFullError(Exception):
    def __init__(self):
        super().__init__('Package is too big to be loaded on the truck.')