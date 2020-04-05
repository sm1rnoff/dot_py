from project.factory.factory import Factory


class EggFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        ingredients = ["chicken egg", "quail egg"]
        if ingredient_type in ingredients:
            if self.can_add(quantity):
                self.ingredients[ingredient_type] = quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(
                f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self):
        pass

    @property
    def products(self):
        pass
