__title__ = 'docts'
__author__ = 'foyoux'
__version__ = '0.0.1'

import argparse


def main():
    epilog = f'%(prog)s({__version__}) by foyoux(https://github.com/foyoux/docts)'
    parser = argparse.ArgumentParser(prog='docts', description='', epilog=epilog)
    parser.add_argument('-v', '--version', action='version', version=epilog)

    parser.parse_args()
