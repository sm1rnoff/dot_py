def makeSound(animal_type):
    return animal_type.sound()


class Cat:
    def sound(self):
        return 'meow'


class Dog:
    def sound(self):
        return 'wuff!'


cat = Cat()
dog = Dog()
print(makeSound(cat))
print(makeSound(dog))
