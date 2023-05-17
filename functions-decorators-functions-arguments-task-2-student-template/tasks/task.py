def union(*args) -> set:
    result = set()
    for arg in args:
        if isinstance(arg, (list, tuple, set)):
            result |= set(arg)
        else:
            raise TypeError(f"Unsupported argument type {type(arg)}")
    return result


def intersect(*args) -> set:
    result = set(args[0])
    for arg in args[1:]:
        if isinstance(arg, (list, tuple, set)):
            result &= set(arg)
        else:
            raise TypeError(f"Unsupported argument type {type(arg)}")
    return result
