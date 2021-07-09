"""
不自动测试
"""
from docts import *

wf: WordsFilter
path: str


def filter_code(word: str):
    """
    过滤不需要翻译, 如代码段, 这不是通用的, 需要针对每一个文档自己调整
    :param word:
    :return:
    """
    word = word.lstrip('&#160;')
    if word == 'begin' \
            or word == 'end' \
            or word == 'goto' \
            or word == 'export' \
            or word == 'Read only' \
            or word == 'Write only' \
            or word == 'void' \
            or word.startswith('function ') \
            or word.startswith('method ') \
            or word.startswith('set ') \
            or word.startswith('prototype ') \
            or word.startswith('export ') \
            or word.startswith('if '):
        return True
    return False


def setup_module():
    global wf, path
    # path = r"InstallShield/HelpLib/HelpLib.xlf"
    # path = r"InstallShield/ISdbg/ISdbg.xlf"
    # path = r"InstallShield/ISXHelp/ISXHelp.xlf"
    # path = r"InstallShield/Langref/Langref.xlf"
    # path = r"InstallShield/MSI/msi.xlf"
    # path = r"InstallShield/Verification/Verification.xlf"
    path = r"InstallShield/Virtual/Virtual.xlf"

    if path.endswith('.xls'):
        words = parse_xls(path)
    else:
        words = parse_xlf(path)
    wf = WordsFilter(words)


def test_words():
    wf.add_filter(filter_not_str)
    wf.add_filter(filter_eq_symbol)
    write_xls(path, wf.words)


def test_ignore():
    wf.add_filter(filter_code)
    write_xls(path, wf.ignores, wf.ignores)
