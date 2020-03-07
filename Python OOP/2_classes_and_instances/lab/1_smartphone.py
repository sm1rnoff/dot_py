class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        #self.is_on = False if self.is_on else True
        self.is_on = not self.is_on
        # if True set to False, if False set to True. Both above does it!

    def install(self, app, memory):
        if self.memory - memory >= 0:
            if self.is_on == True:
                self.memory -= memory
                self.apps.append(app)
                return f'Installing {app}'
            else:
                return f'Turn on your phone to install {app}'
        else:
            return f'Not enough memory to install {app}'

    def status(self):
        total_apps = len(self.apps)
        return f'Total apps: {total_apps}. Memory left: {self.memory}'


#
smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
