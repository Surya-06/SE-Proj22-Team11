# 9/7/22

# standard library imports

from .data import Data;
from .utils import the;

class CSVReader:

    def __init__(self, filepath):
        self.filepath = filepath;

    def processFileContents(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            header = file.readline();
            
            the['data'] = Data(header_string=header);

            for line in file:
                if len(str(line).strip()) == 0:
                    break;
                the['data'].importDataFromLine(line);


