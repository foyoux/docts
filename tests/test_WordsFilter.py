from docts import *

words = [
    'function OnBegin()',
    '&#160;&#160;&#160;&#160;string szFileName, svFontTitle;',
    'begin',
    '&#160;&#160;&#160;&#160;szFileName = FOLDER_FONTS ^ "Estre.ttf";',
    '&#160;&#160;&#160;&#160;svFontTitle = "Estrangelo Edessa";',
    '&#160;&#160;&#160;&#160;RegisterFontResource ( szFileName, svFontTitle, TRUE, REGFONT_OPTION_DEFAULT );',
    '&#160;&#160;&#160;&#160;// If you cut and paste this sample script into a project',
    '&#160;&#160;&#160;&#160;// and run it, the following line aborts execution of the script.',
    '&#160;&#160;&#160;&#160;abort;',
    'end;',
    'InstallShield 2020 Help Library',
    'May 2020',
    '<a href="legal_info.htm">Copyright Information</a> | <a href="http://www.flexera.com" target="_blank">Flexera</a>',
]


def test_add_filter():
    assert WordsFilter(words).add_filter(lambda x: True).words == []
    assert WordsFilter(words).add_filter(lambda x: False).words == words


def test_add_map():
    assert WordsFilter(words).add_map(lambda x: None).words == [None] * len(words)
    assert WordsFilter(words).add_map(lambda x: 'docts').words == ['docts'] * len(words)


def test_add_replace():
    assert WordsFilter(['160 160', 'xxx160xxx']).add_replace('160', '250').words == ['250 250', 'xxx250xxx']


def test_add_contain_filter():
    assert WordsFilter(words).add_contain_filter('160').words == [
        'function OnBegin()',
        'begin',
        'end;',
        'InstallShield 2020 Help Library',
        'May 2020',
        '<a href="legal_info.htm">Copyright Information</a> | <a href="http://www.flexera.com" target="_blank">Flexera</a>',
    ]


def test_add_start_filter():
    assert WordsFilter(words).add_start_filter('&').words == [
        'function OnBegin()',
        'begin',
        'end;',
        'InstallShield 2020 Help Library',
        'May 2020',
        '<a href="legal_info.htm">Copyright Information</a> | <a href="http://www.flexera.com" target="_blank">Flexera</a>',
    ]

    assert WordsFilter(['\t\t123']).add_start_filter('123', '\t').words == []


def test_add_end_filter():
    assert WordsFilter(words).add_end_filter(';').words == [
        'function OnBegin()',
        'begin',
        '&#160;&#160;&#160;&#160;// If you cut and paste this sample script into a project',
        '&#160;&#160;&#160;&#160;// and run it, the following line aborts execution of the script.',
        'InstallShield 2020 Help Library',
        'May 2020',
        '<a href="legal_info.htm">Copyright Information</a> | <a href="http://www.flexera.com" target="_blank">Flexera</a>',
    ]
    assert WordsFilter(['\t\t123']).add_end_filter('12', '3').words == []
