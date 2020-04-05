from abc import ABC, abstractmethod


class Factory(ABC):
    def __init__(self, name: str, capacity: str):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self):
        pass

    @abstractmethod
    def remove_ingredient(self):
        pass

    def can_add(self, value: int):
        return value <= self.capacity
