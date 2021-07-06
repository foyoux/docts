from typing import Callable, List


class WordsFilter:
    def __init__(self, words: List[str]):
        self.words = words
        self.ignores = []

    def add_filter(self, _filter: Callable[[str], bool]):
        words = []
        for word in self.words:
            if _filter(word):
                self.ignores.append(word)
                continue
            words.append(word)
        print(f'过滤文本 {_filter.__name__}: {len(self.words) - len(words)}')
        self.words = words

    def add_words_map(self, _map: Callable[[str], str]):
        self.words = [_map(i) for i in self.words]

    def add_ignores_map(self, _map: Callable[[str], str]):
        self.ignores = [_map(i) for i in self.ignores]

    def add_map(self, _map: Callable[[str], str]):
        self.add_words_map(_map)
        self.add_ignores_map(_map)

    def add_words_replace(self, old, new):
        i: str
        self.words = [i.replace(old, new) for i in self.words]

    def add_ignores_replace(self, old, new):
        i: str
        self.ignores = [i.replace(old, new) for i in self.ignores]

    def add_replace(self, old, new):
        i: str
        self.add_words_replace(old, new)
        self.add_ignores_replace(old, new)
