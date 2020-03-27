class Person:
    def sleep(self):
        return 'sleeping...'


class Employee:
    def get_fired(self):
        return 'fired...'


class Teacher(Person, Employee):
    #    def __init(self):
    #        Person.__init__()
    #        Employee.__init__()

    def teach(self):
        return 'teaching...'


human = Teacher()

print(human.get_fired())
print(human.sleep())
print(human.teach())
