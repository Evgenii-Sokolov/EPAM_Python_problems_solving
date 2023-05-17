from functools import wraps

def decorator_apply(lambda_func):
    def decorator(func2):
        @wraps(func2)
        def wrapper(*args, **kwargs):
                result = lambda_func(*args, **kwargs)
                return func2(result)
        return wrapper
    return decorator

@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num
