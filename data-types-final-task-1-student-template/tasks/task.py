from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    unique_values = set()
    for dictionary in lst:
        for value in dictionary.values():
            unique_values.add(value)
    return unique_values
