import pytest
from src.shop.inventory import Inventory, InventoryItem
from src.shop.shopping_cart import ShoppingCart


@pytest.mark.integration
def test_cannot_add_more_items_than_exist_in_stock():
    inventory = Inventory()
    item = InventoryItem(1, "Keyboard", 499, 2)
    inventory.add_item(item)

    cart = ShoppingCart(inventory)

    result = cart.add_inventory_item(item, 3)

    assert result is False
    assert len(cart.items) == 0
    assert inventory.items[1].amount_in_stock == 2


@pytest.mark.integration
def test_can_add_item_when_stock_is_enough():
    inventory = Inventory()
    item = InventoryItem(1, "Keyboard", 499, 5)
    inventory.add_item(item)

    cart = ShoppingCart(inventory)

    result = cart.add_inventory_item(item, 2)

    assert result is True
    assert len(cart.items) == 1
    assert cart.items[0].amount_in_cart == 2
    assert inventory.items[1].amount_in_stock == 3