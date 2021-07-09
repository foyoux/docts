import os

from docts import *


def test_parse_xlf():
    cdir = os.path.dirname(__file__)
    words = parse_xlf(cdir + r'/test_files/vsintellicode.xlf')
    assert isinstance(words, list)
    assert len(words) == 24
    words = parse_xlf(cdir + r'./test_files/Sisulizer.xlf')
    assert isinstance(words, list)
    assert len(words) == 6679
