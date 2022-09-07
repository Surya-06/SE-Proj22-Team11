#!/usr/bin/env python3

__author__ = "SE Team Project 11 - HW 2"
__version__ = "1.0.0"
__license__ = "MIT"

import utils;
from csv import CSVReader; 


def main():
    print("checking the functionality of the csv reader");
    filepath = 'test.csv';

    csv_reader = CSVReader(filepath);
    csv_reader.processFileContents();


if __name__ == "__main__":
    main()
