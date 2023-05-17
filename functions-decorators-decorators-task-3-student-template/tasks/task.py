import functools
def validate(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        for arg in args + tuple(kwargs.values()):
            if not isinstance(arg, int) or arg < 0 or arg > 256:
                return "Function call is not valid!"
        return "Pixel created!"
    return wrapper

@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"
