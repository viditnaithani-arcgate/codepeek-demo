"""A small in-memory inventory for a shop."""

from dataclasses import dataclass
from typing import List


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

    def average_price(self):
        prices = [item.price for item in self.items.values()]
        if not prices:
            return 0.0
        return sum(prices) / len(prices)

    def find(self, name):
        return self.items.get(name)

    def load_from_file(self, path):
        f = open(path)
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 3:
                raise ValueError(f"Invalid line format: {line}")
            name, quantity, price = parts
            self.add_item(name, int(quantity), float(price))
