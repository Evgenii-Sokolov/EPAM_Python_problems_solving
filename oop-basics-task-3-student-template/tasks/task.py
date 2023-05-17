class Counter:
    def __init__(self, start=0, stop=None):
        self.value = start
        self.stop = stop

    def increment(self):
        if self.stop is None or self.value < self.stop:
            self.value += 1
            if self.stop is not None and self.value == self.stop:
                print("Maximal value is reached.")
        else:
            print("Maximal value is reached.")

    def get(self):
        return self.value