import os

class Cd:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.saved_path = os.getcwd()
        if not os.path.isdir(self.path):
            raise ValueError(f"Directory '{self.path}' does not exist.")
        os.chdir(self.path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.saved_path)