from docts import *

if __name__ == '__main__':
    # path = r"D:\Users\foyou\TODO\InstallShield\MSI\msi.xls"
    # words = parse_xls(path)
    path = r"D:\Users\foyou\TODO\InstallShield\MSI\msi.xlf"
    words = parse_xlf(path)

    wF = WordsFilter(words)
    wF.add_filter(filter_not_str)
    wF.add_filter(filter_upper)
    wF.add_filter(filter_eq_symbol)

    write_xls(path, origins=wF.words)
