import re

UPPER_CHAR = re.compile(r'[A-Z]')
SPACE_SPLIT = re.compile('[ \t]+')


def filter_not_str(word: str) -> bool:
    """
    不存在全小写的字母组合则过滤(return True)
    :param word:
    :return:
    """
    for w in SPACE_SPLIT.split(word):
        if w.isalpha() and not word.isupper() and UPPER_CHAR.search(w) is None:
            return False
    return True


def filter_eq_symbol(word: str) -> bool:
    """
    存在' = ', 则过滤, 一般代码中常见
    :param word:
    :return:
    """
    if word.find('\n') == -1 and word.find(' = ') != -1:
        return True
    return False
