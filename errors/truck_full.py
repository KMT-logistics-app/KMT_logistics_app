class TruckFullError(Exception):
    def __init__(self):
        super().__init__('This truck is full.')