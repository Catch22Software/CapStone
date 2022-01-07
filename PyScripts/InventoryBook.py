from PyScripts.InventoryItem import InventoryItem


class InventoryBook:
    def __init__(self, name=''):
        self.owner_name = name
        self.inventory_book = {}

    def add_item(self, item):
        add_me = InventoryItem(item[0], item[1], item[2])
        self.inventory_book.update({item[0]: add_me})

    def delete_item(self, item_to_delete):
        self.inventory_book.pop(item_to_delete.ITEM_NAME)

    def __str__(self):
        return self.inventory_book.items()

    @staticmethod
    def create_recommendation():
        return "I recommended candy!!"
    # may need to fix formatting
