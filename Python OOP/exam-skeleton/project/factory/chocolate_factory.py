from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        ingredients = ["white chocolate",
                       "dark chocolate", "milk chocolate", "sugar"]
        if ingredient_type in ingredients:
            if self.can_add(quantity):
                self.ingredients[ingredient_type] = quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(
                f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients:
            if quantity <= self.ingredients[ingredient_type]:
                self.ingredients[ingredient_type] = quantity
            else:
                raise ValueError(
                    "Ingredient quantity cannot be less than zero")
        else:
            raise KeyError("No such product in the factory")

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name in self.recipes[recipe_name]:
            if recipe_name in self.products:
                self.products[recipe_name] += 1
            else:
                self.products[recipe_name] = 1
        else:
            raise TypeError("No such recipe")
