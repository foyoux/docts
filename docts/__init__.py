from .filter import WordsFilter
from .filter.F1 import *
from .map.M1 import *
from .parser.XLFParser import parse_xlf
from .parser.XLSParser import parse_xls
from .writer.XLSWriter import write_xls

__title__ = 'docts'

__description__ = 'document translate, read & translate & write'
__url__ = 'https://github.com/foyoux/docts'
__version__ = '0.0.3'
__author__ = 'foyou'
__author_email__ = 'yimi.0822@qq.com'
__license__ = 'GPL-3.0'
__copyright__ = f'Copyright 2021 {__author__}'
__ide__ = 'PyCharm - https://www.jetbrains.com/pycharm/'


def todo(path: str):
    """
    快速尝试
    :param path:
    :return:
    """
    if path.endswith('.xls'):
        words = parse_xls(path)
    else:
        words = parse_xlf(path)
    wf = WordsFilter(words)
    wf.add_filter(filter_not_str)
    wf.add_filter(filter_eq_symbol)
    write_xls(path, wf.words)
