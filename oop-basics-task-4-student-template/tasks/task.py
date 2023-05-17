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


class HistoryDict:
    def __init__(self, data):
        self.data = data
        self.history = []

    def set_value(self, key, value):
        self.data[key] = value
        if key in self.history:
            self.history.remove(key)
        self.history.append(key)
        if len(self.history) > 5:
            self.history.pop(0)

    def get_history(self):
        return self.history