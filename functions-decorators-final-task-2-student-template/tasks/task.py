from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    result = []
    start = 0
    for i in indexes:
        if i < len(s):
            result.append(s[start:i])
            start = i
    result.append(s[start:])
    return result
