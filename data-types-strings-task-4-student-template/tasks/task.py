def check_str(s: str):
    clean_str = "".join(c for c in s if c.isalpha()).lower()
    return clean_str == clean_str[::-1]