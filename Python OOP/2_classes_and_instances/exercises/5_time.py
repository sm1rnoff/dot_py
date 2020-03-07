class Time:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.max_hours = 24
        self.max_minutes = 60
        self.max_seconds = 60

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        print(f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}')

    def next_second(self):
        if self.seconds == 60:
            if self.minutes == 60:
                if self.hours == 24:
                    self.set_time(0, 0, 0)
                self.set_time(self.hours+1, 0, 0)
            self.set_time(self.hours, self.minutes+1, 0)
        self.set_time(self.hours, self.minutes, self.seconds+1)
        self.get_time()


time = Time(9, 30, 60)
print(time.next_second())
