from item_status import ItemStatus
from board_item import BoardItem
from board import Board
from event_log import EventLog
from datetime import date, timedelta


def add_days_to_now(d):
    return date.today() + timedelta(days=d)
