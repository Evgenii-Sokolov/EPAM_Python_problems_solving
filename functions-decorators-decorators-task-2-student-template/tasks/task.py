import datetime

def log(fn):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = fn(*args, **kwargs)
        end_time = datetime.datetime.now()
        with open('log.txt', 'a') as f:
            f.write(f'{fn.__name__}; args: {", ".join([f"{arg}={repr(value)}" for arg, value in enumerate(args)])}; kwargs: {", ".join([f"{key}={repr(value)}" for key, value in kwargs.items()])}; execution time: {end_time - start_time}\n')
        return result
    return wrapper