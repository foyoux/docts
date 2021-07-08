from typing import List

import xlwings as xw


def parse_xls(xls_path: str, sheet_index: int = 0, column: int = 0) -> List[str]:
    """
    解析xls, 获取字符串
    :param xls_path:
    :param sheet_index:
    :param column:
    :return:
    """
    if not xls_path.endswith('.xls'):
        print(f'不是xlf文件: {xls_path}')
        raise

    app = xw.App(add_book=False)
    wb = app.books.open(xls_path)
    sheet = wb.sheets[sheet_index]
    used = sheet.used_range
    origen_words = used.columns[column].value

    # 过滤重复
    olen = len(origen_words)
    # words = [i for i in set(origen_words) if i != '' and isinstance(i, str)]
    words = [i for i in set(origen_words) if i != '']
    print(f'过滤重复或空文本 parse_xls: {len(origen_words) - len(words)}')

    # 关闭
    wb.close()
    app.quit()
    return words
