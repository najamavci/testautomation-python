class InventoryItem:
    def __init__(self, id, name, price, amount_in_stock):
        self.id = id
        self.name = name
        self.price = price
        self.amount_in_stock = amount_in_stock


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.id] = item

    def has_enough(self, item_id, amount):
        item = self.items.get(item_id)
        return item is not None and item.amount_in_stock >= amount

    def reduce_stock(self, item_id, amount):
        if not self.has_enough(item_id, amount):
            return False
        self.items[item_id].amount_in_stock -= amount
        return True