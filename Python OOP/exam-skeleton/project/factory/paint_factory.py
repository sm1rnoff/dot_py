from project.factory.factory import Factory


class PaintFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        ingredients = ["white", "yellow", "blue", "green", "red"]
        if ingredient_type in ingredients:
            if self.can_add(quantity):
                if ingredient_type in self.ingredients:
                    self.ingredients[ingredient_type] += quantity
                else:
                    self.ingredients[ingredient_type] = quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(
                f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients:
            if quantity <= self.ingredients[ingredient_type]:
                self.ingredients[ingredient_type] -= quantity
            else:
                raise ValueError(
                    "Ingredient quantity cannot be less than zero")
        else:
            raise KeyError("No such ingredient in the factory")

    @property
    def products(self):
        return self.ingredients
#        return [print(key) for key in self.ingredients.keys()]
