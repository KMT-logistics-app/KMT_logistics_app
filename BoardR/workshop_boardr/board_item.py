from datetime import date, timedelta
from item_status import ItemStatus
from event_log import EventLog


def add_days_to_now(d):
    return date.today() + timedelta(days=d)


class BoardItem:
    def __init__(self, title: str, due_date: date):
        self.title = title
        self.due_date = due_date
        self.__status = ItemStatus.OPEN
        self.__history = [
            EventLog(f"Item created: {self.title}, [{self.__status} | {self.due_date}]")
        ]

    @property
    def status(self):
        return self.__status

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if 5 <= len(value) <= 30:
            if hasattr(self, "__history"):
                self.__history.append(
                    EventLog(f"Title changed from {self.title} to {value}")
                )
            self.__title = value
        else:
            raise ValueError("Title must be string between 5 and 30 characters!")

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        if value > date.today():
            if hasattr(self, "__history"):
                self.__history.append(
                    EventLog(f"DueDate changed from {self.due_date} to {value}")
                )
            self.__due_date = value
        elif value <= date.today():
            raise ValueError("Due_date has to be in the future!")

    def advance_status(self):
        if self.status == ItemStatus.next(self.status):
            self.__history.append(
                EventLog(f"Cant change status, already at {self.status}")
            )
        else:
            self.__history.append(
                EventLog(
                    f"Status changed from {self.status} to {ItemStatus.next(self.status)}"
                )
            )
        self.__status = ItemStatus.next(self.status)

    def revert_status(self):
        if self.status == ItemStatus.previous(self.status):
            self.__history.append(
                EventLog(f"Cant change status, already at {self.status}")
            )
        else:
            self.__history.append(
                EventLog(
                    f"Status changed from {self.status} to {ItemStatus.previous(self.status)}"
                )
            )
        self.__status = ItemStatus.previous(self.status)

    def info(self):
        return f"{self.title}, [{self.status} | {self.due_date}]"

    def history(self):
        history = ""
        for his in self.__history:
            history += f"\n{his._timestamp} {his._description}"
        return history
