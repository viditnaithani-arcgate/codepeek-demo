import unittest

from inventory import Inventory


class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()
        self.inv.add_item("pen", 10, 1.5)
        self.inv.add_item("book", 2, 12.0)

    def test_total_value(self):
        self.assertEqual(self.inv.total_value(), 39.0)

    def test_add_existing_item_increases_quantity(self):
        self.inv.add_item("pen", 5, 1.5)
        self.assertEqual(self.inv.find("pen").quantity, 15)

    def test_remove_item(self):
        self.inv.remove_item("pen", 4)
        self.assertEqual(self.inv.find("pen").quantity, 6)

    def test_remove_all_deletes_item(self):
        self.inv.remove_item("book", 2)
        self.assertIsNone(self.inv.find("book"))

    def test_cannot_remove_more_than_stock(self):
        with self.assertRaises(ValueError):
            self.inv.remove_item("book", 3)


if __name__ == "__main__":
    unittest.main()
