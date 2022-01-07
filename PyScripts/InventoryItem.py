from enum import Enum


class Usage(Enum):
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3
    RARELY = 4


class InventoryItem:
    def __init__(self, item_name, usage, qty):
        self.ITEM_NAME = str(item_name)
        self.item_usage = usage.name if isinstance(usage, Usage) else Usage.DAILY
        self.item_qty = int(qty)

    def update_usage(self, new_usage):
        self.item_usage = new_usage.name if isinstance(new_usage, Usage) else Usage.DAILY

    def update_quantity(self, amount):
        self.item_qty = int(amount)

    def __str__(self):
        return "Item Name: %s\nItem Usage: %s\nItem QTY: %d" % (self.ITEM_NAME, self.item_usage, self.item_qty)
