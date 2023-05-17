from typing import Union

def divide(str_with_ints: str) -> Union[float, str]:
    try:
        a, b = map(int, str_with_ints.split())
        return a / b
    except ZeroDivisionError:
        return "Error code: division by zero"
    except ValueError as e:
        return f"Error code: {str(e)}"