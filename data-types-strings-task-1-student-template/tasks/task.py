def get_fractions(a_b: str, c_b: str) -> str:
    a, b = a_b.split('/')
    c, b = c_b.split('/')
    bint = int(b)
    a_c = int(a) + int(c)
    sumsum = f"{a_b} + {c_b} = {a_c}/{bint}"
    print(f"{a_b} + {c_b} = {a_c}/{bint}")
    return sumsum
