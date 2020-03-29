class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __repr__(self):
        return f'{self.username} of type {self.__class__.__name__} has level {self.level}'


class Elf(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)


class MuseElf(Elf):
    def __init__(self, username, level):
        super().__init__(username, level)


class Wizard(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)


class DarkWizard(Wizard):
    def __init__(self, username, level):
        super().__init__(username, level)


class SoulMAster(DarkWizard):
    def __init__(self, username, level):
        super().__init__(username, level)


class Knight(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)


class DarkKnight(Knight):
    def __init__(self, username, level):
        super().__init__(username, level)


class BladeKnight(DarkKnight):
    def __init__(self, username, level):
        super().__init__(username, level)


h = Hero('heroto', 'heroic')
e = MuseElf('elf_name', 'high')
print(h.__repr__())
print(e.__repr__())
