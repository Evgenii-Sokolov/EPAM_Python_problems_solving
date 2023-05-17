
def get_longest_word(s: str) -> str:
    longestword = max(s.split(), key=len)
    return longestword



