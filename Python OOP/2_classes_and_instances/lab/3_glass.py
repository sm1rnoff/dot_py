class Glass:
    #capacity = 250

    def __init__(self):
        self.content = 0
        self.capacity = 250

    def fill(self, ml):
        if self.content + ml <= self.capacity:
            self.content += ml
            return f'Glass filled with {ml} ml'
        return f'Cannot add {ml} ml'

    def empty(self):
        self.content = 0
        return f'Glass is now empty'

    def info(self):
        left_space = self.capacity - self.content
        return f'{left_space} ml left'


#
glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
