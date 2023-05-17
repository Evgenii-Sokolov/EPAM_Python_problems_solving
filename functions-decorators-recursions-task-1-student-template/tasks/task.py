from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    result = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            result += seq_sum(element)
        else:
            result += element
    return result

