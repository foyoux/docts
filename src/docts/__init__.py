__title__ = 'docts'
__author__ = 'foyoux'
__version__ = '0.0.1'
__description__ = 'document translate, read & translate & write'
__url__ = 'https://github.com/foyoux/docts'
__author_email__ = 'yimi.0822@qq.com'
__license__ = 'GPL-3.0'
__copyright__ = f'Copyright 2021-2023 {__author__}'
__ide__ = 'PyCharm - https://www.jetbrains.com/pycharm/'

import argparse
import html
import re
from typing import Callable, Pattern, AnyStr, List

from pygtrans import Translate, Null

# filter start

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


# filter end


# map start

def map_symbol_dot(word: str) -> str:
    """
    简单映射器, 如果内容未为utf-8点号, 则替换(返回), gb2312的
    :param word:
    :return:
    """
    if word == '•':
        return '●'


# map end


def parse_xlf(xlf_path: str) -> List[str]:
    """
    解析xlf文件, 获取原文字符串
    :param xlf_path:
    :return:
    """
    if not xlf_path.endswith('.xlf'):
        print(f'不是xlf文件: {xlf_path}')
        raise

    # newline='', 换行符原样读入
    with open(xlf_path, encoding='utf-8', newline='') as f:
        txt = f.read()
        origen_words = re.findall(r'<source[^>]*>(.*?)</source>', txt, re.DOTALL)
        del txt

    i: str
    # words = [html.unescape(i.replace('[]\n', '\r\n')) for i in set(origen_words) if i != '']
    words = [html.unescape(i) for i in set(origen_words) if i != '']

    print(f'过滤重复或空文本 parse_xlf: {len(origen_words) - len(words)}')

    return words


def write_xlf(xlf_path: str, origins: List[str], client: Translate, trans: List[str] = None):
    # 翻译
    if trans is None:
        trans = client.translate(origins)
        if isinstance(trans, Null):
            print(trans.msg)
            raise
        trans = [i.translatedText for i in trans]

    # 写入文件
    with open(xlf_path, 'w', encoding='utf-8', newline='') as f:
        f.write(
            '<?xml version="1.0" encoding="utf-8"?>\n'
            '<xliff version="1.2" xmlns="urn:oasis:names:tc:xliff:document:1.2" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
            'xsi:schemaLocation="urn:oasis:names:tc:xliff:document:1.2 xliff-core-1.2-strict.xsd">\n'
            '  <file original="Sisulizer" datatype="unknown" source-language="en-US" target-language="zh-CN">\n'
            '    <body>\n'
            '      <group id="root" datatype="unknown">\n'
            '        '
        )
        for a, b in zip(origins, trans):
            f.write(
                '<trans-unit>\n'
                f'          <source>{html.escape(a)}</source>\n'
                f'          <target>{html.escape(b)}</target>\n'
                '        </trans-unit>\n'
                '        '
            )
        f.write(
            '      </group>\n'
            '    </body>\n'
            '  </file>\n'
            '</xliff>'
        )


class Docts:

    def __init__(self, xlf_path: str, client: Translate):
        self.xlf_path = xlf_path
        self.words = parse_xlf(xlf_path)
        self.ignores = []
        self.client = client

    def add_filter(self, _filter: Callable[[str], bool]):
        """
        添加过滤器, 排除某些无需导出的内容
        :param _filter:
        :return:
        """
        words = []
        for word in self.words:
            if _filter(word):
                self.ignores.append(word)
                continue
            words.append(word)
        print(f'过滤文本 {_filter.__name__}: {len(self.words) - len(words)}')
        self.words = words
        return self

    def add_contain_filter(self, contain: Pattern[AnyStr]):
        """
        支持正则表达式
        :param contain:
        :return:
        """
        words = []
        for word in self.words:
            if re.search(contain, word):
                self.ignores.append(word)
                continue
            words.append(word)
        print(f'过滤文本 add_contain_filter({contain}): {len(self.words) - len(words)}')
        self.words = words
        return self

    def add_start_filter(self, start: str, strip: str = None):
        words = []
        word: str
        for word in self.words:
            if strip:
                word = word.lstrip(strip)
            if word.startswith(start):
                self.ignores.append(word)
                continue
            words.append(word)
        print(f'过滤文本 add_start_filter({start}): {len(self.words) - len(words)}')
        self.words = words
        return self

    def add_end_filter(self, end: str, strip: str = None):
        words = []
        word: str
        for word in self.words:
            if strip:
                word = word.rstrip(strip)
            if word.endswith(end):
                self.ignores.append(word)
                continue
            words.append(word)
        print(f'过滤文本 add_end_filter({end}): {len(self.words) - len(words)}')
        self.words = words
        return self

    def add_map(self, _map: Callable[[str], str]):
        """
        添加自定义映射器, 参考 def map_symbol_dot
        :param _map:
        :return:
        """
        self.words = [_map(i) for i in self.words]
        return self

    def add_replace(self, old, new):
        """
        全局全部替换, 也可以使用 add_map 实现, 这种不需要写函数
        :param old:
        :param new:
        :return:
        """
        i: str
        self.words = [i.replace(old, new) for i in self.words]
        return self

    def reset(self):
        self.words.extend(self.ignores)
        return self

    def save_words(self):
        """..."""
        xlf_path = self.xlf_path[:-4] + '_words.xlf'
        write_xlf(xlf_path, self.words, self.client)
        return xlf_path

    def save_ignores(self):
        """..."""
        xlf_path = self.xlf_path[:-4] + '_ignores.xlf'
        write_xlf(xlf_path, self.ignores, self.client, self.ignores)
        return xlf_path


def main():
    epilog = f'%(prog)s({__version__}) by foyoux(https://github.com/foyoux/docts)'
    parser = argparse.ArgumentParser(prog='docts', description='', epilog=epilog)
    parser.add_argument('-v', '--version', action='version', version=epilog)

    parser.parse_args()
