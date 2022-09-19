#!/usr/bin/env python3

__author__ = "SE Team Project 11 - HW 2"
__version__ = "1.0.0"
__license__ = "MIT"

import sys
from os import path;

if __package__ is None:
    sys.path.append(path.dirname( path.dirname( path.abspath(__file__) )))

from cmd import *
from utils import *
from data import Data
from Test.test_eg import *

def main():
    # Should always be in the beginning
    parse_command_line()

    # Process switches in the below priority order
    if the['show_help'] == True:
        print_help_message()
        # return

    if the['filepath']:    
        d = Data(the['filepath'])

    if the['eg'] is not None:
        if the['eg'] in ('eg_sym', 'egSym'):
            eg_sym()
        elif the['eg'] in ('eg_the','egThe'):
            eg_the()
        elif the['eg'] in ('eg_num','egNum'):
            eg_num()
        elif the['eg'] in ('eg_Bignum','egBignum'):
            eg_Bignum()
        elif the['eg'] in ('eg_csv','egCSV'):
            eg_csv()
        elif the['eg'] in ('eg_data','egData'):
            eg_data()
        elif the['eg'] in ('eg_stats','egStats'):
            eg_stats()        
        elif the['eg'] in ('all', 'All'):
            eg_sym()
            eg_the()
            eg_num()
            eg_Bignum()
            eg_csv()
            eg_data()
            eg_stats()

        
if __name__ == "__main__":
    main()
