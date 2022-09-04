# SE HW - 2

import math


class Sym:
    def __init__(self, column_name, column_position):
        self.column_name = column_name
        self.column_position = column_position
        self.data = list()
        self.freq_count = dict()

    def add(self, value):
        self.data.append(value);
        if value in self.freq_count:
            self.freq_count[value]+=1;
        else:
            self.freq_count[value]=1;

    def mid(self):
        return max(self.freq_count, key=self.freq_count.get);

    def div(self):
        e = 0
        for _, n in self.freq_count.items():
            p = n / len(self.data)
            e = e - (p*math.log(p,2))
        return e

    def getColumnName(self):
        return self.column_name;
    
    def getColumnPosition(self):
        return self.column_position;

    def getData(self):
        return self.data;




