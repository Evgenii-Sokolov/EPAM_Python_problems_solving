from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    unique_words = sorted(set(str_list))
    return list(unique_words)
