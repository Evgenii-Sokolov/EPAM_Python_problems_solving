def replacer(s: str) -> str:
    return s.replace("'", "_t_").replace('"', "'").replace("_t_", '"')