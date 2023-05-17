from typing import List

def split(data: str, sep=None, maxsplit=-1):
    if sep is None:
        sep = ' '
    substrings = []
    start = 0
    count = 0
    for i, char in enumerate(data):
        if char == sep:
            substrings.append(data[start:i])
            start = i + 1
            count += 1
            if count == maxsplit:
                break
    substrings.append(data[start:])
    return substrings
