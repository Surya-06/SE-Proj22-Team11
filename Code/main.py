#!/usr/bin/env python3

__author__ = "SE Team Project 11 - HW 2"
__version__ = "1.0.0"
__license__ = "MIT"

from cmd import *;
from utils import *;
from csv import CSVReader; 


def main():
    # Should always be in the beginning
    parseCommandLine();

    # Process switches in the below priority order
    if the['show_help'] or len(the['filepath']) == 0:
        printHelpMessage();
        return;
    
    csv_reader = CSVReader();
    csv_reader.processFileContents();
    # TODO: Add further processing etc.

    for item in the['data'].columns:
        print(item._has)


if __name__ == "__main__":
    main()
