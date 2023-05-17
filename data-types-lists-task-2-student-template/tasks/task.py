from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    list_empty = []
    for i in range(1, n+1):
        if not i % 3 and not i % 5:
            list_empty.append("FizzBuzz")
        elif not i % 3:
            list_empty.append("Fizz")
        elif not i % 5:
            list_empty.append("Buzz")
        else:
            list_empty.append(i)
    return list_empty

