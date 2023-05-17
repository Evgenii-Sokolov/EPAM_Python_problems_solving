from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
    def __add__(self, other: str) -> List[str]:
        return [f"{val} {other}" for val in self.values]
