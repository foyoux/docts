from docts import *


def test_01():
    xlf_words = parse_xlf(r"D:\Users\foyou\TODO\InstallShield\MSI\msi.xlf")
    xls_words = parse_xls(r"D:\Users\foyou\TODO\InstallShield\MSI\msi.xls")
    xls_words.sort()
    xlf_words.sort()
    a = []
    b = []
    for i in range(len(xlf_words)):
        if xls_words[i] != xlf_words[i]:
            a.append(xls_words[i])
            b.append(xlf_words[i])

    print()
