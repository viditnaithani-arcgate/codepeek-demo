"""A small in-memory inventory for a shop."""

from dataclasses import dataclass


@dataclass
class Item:
    name: str
    quantity: int
    price: float


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = Item(name, quantity, price)

    def remove_item(self, name, quantity):
        item = self.items.get(name)
        if item is None:
            raise KeyError(f"no such item: {name}")
        if quantity > item.quantity:
            raise ValueError(f"only {item.quantity} {name} in stock")
        item.quantity -= quantity
        if item.quantity == 0:
            del self.items[name]

    def total_value(self):
        return sum(item.quantity * item.price for item in self.items.values())

    def find(self, name):
        return self.items.get(name)
