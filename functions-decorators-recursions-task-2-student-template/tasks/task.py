from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    result = []
    for element in sequence:
        if isinstance(element, (list, tuple)):
            result.extend(linear_seq(element))
        else:
            result.append(element)
    return result
