from docts import *

wf: WordsFilter
path: str


def filter_code(word: str):
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
    # path = r"D:\Users\foyou\TODO\InstallShield\HelpLib\HelpLib.xlf"
    # path = r"D:\Users\foyou\TODO\InstallShield\ISdbg\ISdbg.xlf"
    # path = r"D:\Users\foyou\TODO\InstallShield\ISXHelp\ISXHelp.xlf"
    # path = r"D:\Users\foyou\TODO\InstallShield\Langref\Langref.xlf"
    # path = r"D:\Users\foyou\TODO\InstallShield\MSI\msi.xlf"
    path = r"D:\Users\foyou\TODO\InstallShield\Verification\Verification.xlf"
    path = r"D:\Users\foyou\TODO\InstallShield\Virtual\Virtual.xlf"

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
