class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


f = Person('person', 37)
a = Child('child', 1)
print(f.age)
print(a.age)
print(a.name)
