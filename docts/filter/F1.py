import re

UPPER_CHAR = re.compile(r'[A-Z]')
SPACE_SPLIT = re.compile('[ \t]+')


def filter_not_str(word: str) -> bool:
    for w in SPACE_SPLIT.split(word):
        if w.isalpha() and not word.isupper() and UPPER_CHAR.match(w) is None:
            return False
    return True


def filter_eq_symbol(word: str) -> bool:
    if word.find('\n') == -1 and word.find(' = ') != -1:
        return True
    return False
