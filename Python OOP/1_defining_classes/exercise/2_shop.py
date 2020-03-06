class Shop:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items  # [item for item in items]

    def get_items_count(self):
        return len(self.items)


class Shop:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


# test here...
shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
