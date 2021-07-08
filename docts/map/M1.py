def map_symbol_dot(word: str) -> str:
    """
    简单映射器, 如果内容未为utf-8点号, 则替换(返回), gb2312的
    :param word:
    :return:
    """
    if word == '•':
        return '●'
