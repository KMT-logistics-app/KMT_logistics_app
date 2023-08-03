from board_item import BoardItem
from datetime import date, timedelta


def add_days_to_now(d):
    return date.today() + timedelta(days=d)


class Board:
    def __init__(self):
        self._items = []
        self.count = 0

    @property
    def items(self):
        return self._items

    def add_item(self, item: BoardItem):
        if not item in self._items:
            self.items.append(item)
            self.count += 1
        else:
            raise ValueError("Item already in the list")

    def count(self):
        return len(self._items)
