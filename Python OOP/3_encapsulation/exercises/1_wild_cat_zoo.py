class Lion:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 50

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


class Tiger:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 45

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


class Cheetah:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 60

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'

# done with animals, workers starts below


class Keeper:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.salary = salary
        self.age = age

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


class Caretaker:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.salary = salary
        self.age = age

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


class Vet:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.salary = salary
        self.age = age

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'

# done with workers, action classes start below


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if isinstance(animal, Lion) or isinstance(animal, Tiger) or isinstance(animal, Cheetah):
            if self.__animal_capacity - 1 >= 0 and self.__budget - price >= 0:
                self.animals.append(animal)
                self.__animal_capacity -= 1
                self.__budget -= price
                return f'{self.name} the {animal.__class__.__name__} added to the Zoo'
            elif self.__animal_capacity - 1 >= 0 and self.__budget - price < 0:
                return 'Not enough budget'
            else:
                return 'Not enough space for animal'

    def hire_worker(self, worker):
        if isinstance(worker, Keeper) or isinstance(worker, Caretaker) or isinstance(worker, Vet):
            if self.__workers_capacity - 1 >= 0:
                self.workers.append(worker)
                self.__workers_capacity -= 1
                return f'{worker} the {worker.__class__.__name__} hired successfully'
            return 'Not space for worker'

    def fire_worker(self, worker_name):
        if worker_name in self.workers:
            self.workers.remove(worker_name)
            return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salary_expedenture = 0
        for worker in self.workers:
            total_salary_expedenture += worker.salary

        budget_left = self.__budget - total_salary_expedenture

        if budget_left >= 0:
            self.__budget = budget_left
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_tend_expedenture = 0
        for animal in self.animals:
            total_tend_expedenture += animal.get_needs()

        budget_left = self.__budget - total_tend_expedenture

        if budget_left >= 0:
            self.__budget = budget_left
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions_total = 0
        tigers_total = 0
        cheetah_total = 0
        result = f'You have {len(self.animals)} animals\n'
        for animal in self.animals:
            if isinstance(animal, Lion):
                lions_total += 1
            elif isinstance(animal, Tiger):
                tigers_total += 1
            else:
                cheetah_total += 1

        if lions_total > 0:
            result += f'----- {lions_total} Lions:\n'
            for animal in self.animals:
                if isinstance(animal, Lion):
                    result += f'{animal.__repr__()}\n'

        if tigers_total > 0:
            result += f'----- {tigers_total} Tigers:\n'
            for animal in self.animals:
                if isinstance(animal, Tiger):
                    result += f'{animal.__repr__()}\n'

        if cheetah_total > 0:
            result += f'----- {cheetah_total} Cheethas:\n'
            for animal in self.animals:
                if isinstance(animal, Cheetah):
                    result += f'{animal.__repr__()}\n'

        return result

    def workers_status(self):
        keepers_total = 0
        caretakers_total = 0
        vets_total = 0
        result = f'You have {len(self.animals)} workers\n'
        for worker in self.workers:
            if isinstance(worker, Keeper):
                keepers_total += 1
            elif isinstance(worker, Caretaker):
                caretakers_total += 1
            else:
                vets_total += 1

        if keepers_total > 0:
            result += f'----- {keepers_total} Keepers:\n'
            for worker in self.workers:
                if isinstance(worker, Keeper):
                    result += f'{worker.__repr__()}\n'

        if caretakers_total > 0:
            result += f'----- {caretakers_total} Caretakers:\n'
            for worker in self.workers:
                if isinstance(worker, Caretaker):
                    result += f'{worker.__repr__()}\n'

        if vets_total > 0:
            result += f'----- {vets_total} Vets:\n'
            for worker in self.workers:
                if isinstance(worker, Vet):
                    result += f'{worker.__repr__()}\n'

        return result


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion(
    "Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker(
    "Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
