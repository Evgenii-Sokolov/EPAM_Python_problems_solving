from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    dict = {}
    for char in s:
        char = char.lower()
        if char.isalpha() or char.isspace():
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
    return dict
