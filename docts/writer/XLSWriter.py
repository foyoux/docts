from typing import List

import xlwings as xw
from pygtrans import Translate, Null


def write_xls(xls_path: str, origins: List[str], trans: List[str] = None, step=60000):
    """
    写入原文和翻译到xls工作表
    :param xls_path:
    :param origins:
    :param trans:
    :param step:
    :return:
    """
    # if not xls_path.endswith('.xls'):
    #     print(f'不是xlf文件: {xls_path}')
    #     raise

    if trans is None:
        client = Translate()
        trans = client.translate(origins)
        if isinstance(trans, Null):
            print(trans.msg)
            raise
        trans = [i.translatedText for i in trans]

    app = xw.App(add_book=False)
    ol = len(origins)
    step = min(step, 60000)

    for i in range(0, ol, step):
        stop = min(i + step, ol)
        wb = app.books.add()
        sheet = wb.sheets[0]
        # 设置全局格式为 文本
        sheet.cells.number_format = '@'
        sheet.range('A1').options(transpose=True).value = origins[i:stop]
        sheet.range('B1').options(transpose=True).value = trans[i:stop]
        new_wb = f'{xls_path[:-4]}_{i}~{stop}.xls'
        wb.save(new_wb)
        wb.close()
        print(f'保存文件: {new_wb}')

    app.quit()
    return xls_path
