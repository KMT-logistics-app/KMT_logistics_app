import datetime


class EventLog:
    def __init__(self, description):
        self._description = description
        self._timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def info(self):
        return f"[{self._timestamp}] {self._description}"
