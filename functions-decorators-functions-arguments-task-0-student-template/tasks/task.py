from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    return {i: i*i for i in range(1, num+1)}
