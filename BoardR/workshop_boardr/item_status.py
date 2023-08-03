class ItemStatus:
    OPEN = "Open"
    TODO = "Todo"
    IN_PROGRESS = "In progress"
    DONE = "Done"
    VERIFIED = "Verified"

    @classmethod
    def next(cls, current):
        if current == cls.OPEN:
            return cls.TODO
        elif current == cls.TODO:
            return cls.IN_PROGRESS
        elif current == cls.IN_PROGRESS:
            return cls.DONE
        elif current == cls.DONE:
            return cls.VERIFIED
        elif current == cls.VERIFIED:
            return cls.VERIFIED

    @classmethod
    def previous(cls, current):
        if current == cls.OPEN:
            return cls.OPEN
        elif current == cls.TODO:
            return cls.OPEN
        elif current == cls.IN_PROGRESS:
            return cls.TODO
        elif current == cls.DONE:
            return cls.IN_PROGRESS
        elif current == cls.VERIFIED:
            return cls.DONE
