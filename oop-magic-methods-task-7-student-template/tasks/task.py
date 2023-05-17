from contextlib import ContextDecorator
from datetime import datetime, timedelta

class LogFile(ContextDecorator):
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = datetime.now()
        delta = self.end_time - self.start_time
        with open(self.log_file_name, 'a') as log_file:
            log_file.write(f'Start: {self.start_time} | Run: {delta} | An error occurred: {exc_value}\n')
        if exc_type is not None:
            return False
        return True

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return wrapped
