import re


def filter_not_str(word: str) -> bool:
    for w in re.split('[ \t]+', word):
        if w.isalpha():
            return False
    return True


def filter_upper(word: str) -> bool:
    return word.isupper()


def filter_eq_symbol(word: str) -> bool:
    if word.find('\n') == -1 and word.find(' = ') != -1:
        return True
    return False
