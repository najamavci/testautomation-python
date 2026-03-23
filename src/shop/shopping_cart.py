class CartItem:
    def __init__(self, id, name, price, amount_in_cart):
        self.id = id
        self.name = name
        self.price = price
        self.amount_in_cart = amount_in_cart


class ShoppingCart:
    def __init__(self, inventory):
        self.inventory = inventory
        self.items = []

    def add_inventory_item(self, item, amount):
        if not self.inventory.has_enough(item.id, amount):
            return False

        self.inventory.reduce_stock(item.id, amount)
        cart_item = CartItem(item.id, item.name, item.price, amount)
        self.items.append(cart_item)
        return True