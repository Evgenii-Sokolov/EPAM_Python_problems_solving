from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    if len(lst) <= 1:
        return []
    return [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]
