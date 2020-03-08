class Time:
    max_hours = 24
    max_minutes = 60
    max_seconds = 60

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

    def next_second(self):
        if self.seconds + 1 >= self.max_seconds:
            self.seconds = 0
            if self.minutes + 1 >= self.max_minutes:
                self.minutes = 0
                if self.hours + 1 >= self.max_hours:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1
        return self.get_time()


time = Time(9, 30, 60)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(24, 59, 59)
print(time.next_second())
