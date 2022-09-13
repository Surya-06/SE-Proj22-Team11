#!/usr/bin/env python3

__author__ = "SE Team Project 11 - HW 2"
__version__ = "1.0.0"
__license__ = "MIT"

from cmd import *
from utils import *
from data import Data

def main():
    # Should always be in the beginning
    parse_command_line()

    # Process switches in the below priority order
    if the['show_help'] or len(the['filepath']) == 0:
        print_help_message()
        return
        
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
    else:
         eg_sym()
         eg_the()
         eg_num()
         eg_Bignum()
        
        
if __name__ == "__main__":
    main()
