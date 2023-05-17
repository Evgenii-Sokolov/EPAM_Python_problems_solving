from typing import List, Dict

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    result = {}
    for d in args:
        for key, value in d.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result
