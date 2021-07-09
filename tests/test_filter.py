from docts import *

def test_filter_not_str():
    assert filter_not_str('Dcots')
    assert filter_not_str('dOCTS')
    assert filter_not_str('DOCTS')
    assert filter_not_str('Widnows 11')
    assert filter_not_str(' Docts \t ')
    assert filter_not_str('_SummaryInformation')
    assert filter_not_str('Build date: 8/13/2009')
    assert filter_not_str('A Localization Example')
    assert filter_not_str('•')
    assert filter_not_str('MEDIA_FLAG_FORMAT_PATCH')
    assert filter_not_str('OnIISComponentInstalled ( szComponent );')


def test_filter_eq_symbol():
    assert filter_eq_symbol(' = ')
    assert filter_eq_symbol('&#160;&#160;&#160;&#160;svFontTitle = "Estrangelo Edessa";')
    assert filter_eq_symbol('&#160;&#160;&#160;&#160;szFileName = FOLDER_FONTS ^ "Estre.ttf";')



