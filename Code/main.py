#!/usr/bin/env python3

__author__ = "SE Team Project 11 - HW 2"
__version__ = "1.0.0"
__license__ = "MIT"

from .csv import CSVReader; 


def main():
    filepath = '';
    csv_reader = CSVReader(filepath);
    csv_reader.processFileContents();


if __name__ == "__main__":
    main()
