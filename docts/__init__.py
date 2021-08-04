from .filter import *
from .map import *
from .Doc import Doc

__title__ = 'docts'

__description__ = 'document translate, read & translate & write'
__url__ = 'https://github.com/foyoux/docts'
__version__ = '0.0.1'
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
    doc = Doc(path)
    doc.add_filter(filter_eq_symbol)
    doc.add_filter(filter_not_str)
    doc.save_words()
