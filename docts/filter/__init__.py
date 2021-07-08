from typing import Callable, List


class WordsFilter:
    def __init__(self, words: List[str]):
        self.words = words
        self.ignores = []

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

    def add_map(self, _map: Callable[[str], str]):
        """
        添加自定义映射器, 参考 docts/map/M1.py
        :param _map:
        :return:
        """
        self.words = [_map(i) for i in self.words]

    def add_replace(self, old, new):
        """
        全局全部替换, 也可以使用 add_map 实现, 这种不需要写函数
        :param old:
        :param new:
        :return:
        """
        i: str
        self.words = [i.replace(old, new) for i in self.words]
