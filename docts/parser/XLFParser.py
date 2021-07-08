import html
import re
from typing import List


def parse_xlf(xlf_path: str) -> List[str]:
    """
    解析xlf文件, 获取原文字符串
    :param xlf_path:
    :return:
    """
    if not xlf_path.endswith('.xlf'):
        print(f'不是xlf文件: {xlf_path}')
        raise

    with open(xlf_path, encoding='utf-8') as f:
        txt = f.read()
        origen_words = re.findall(r'<source>(.*?)</source>', txt, re.DOTALL)
        del txt

    i: str
    words = [html.unescape(i.replace('\n', '\r\n')) for i in set(origen_words) if i != '']

    print(f'过滤重复或空文本 parse_xlf: {len(origen_words) - len(words)}')

    return words
