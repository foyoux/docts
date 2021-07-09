"""
不自动测试
"""
from docts import *


def test_parse_xls():
    words = parse_xls(r'test_files/htmlhelp.xls')
    assert isinstance(words, list)
    assert len(words) == 7053
