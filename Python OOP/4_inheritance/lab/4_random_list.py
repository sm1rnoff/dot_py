import random


class RandomList(list):
    def get_random_element(self):
        index = random.randint(0, len(self)-1)
        return self.pop(index)


some_list = [1, 2, 3, 4, 5, 6]
lst = RandomList(some_list)
print(lst.get_random_element())
