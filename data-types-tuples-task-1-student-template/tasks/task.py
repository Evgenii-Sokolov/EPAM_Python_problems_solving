from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    digits = []
    while num > 0:
        num, remainder = divmod(num, 10)
        digits.append(remainder)
    digits.reverse()
    return tuple(digits)
