# SE HW - 2

import math

class Sym:
    def __init__(self, c = 0, s = ''):
        self.name = s
        self.at = c
        self.data = list()
        self._has = dict()

    def add(self, value):
        self.data.append(value);
        if value in self._has:
            self._has[value]+=1;
        else:
            self._has[value]=1;

    def mid(self):
        return max(self._has, key=self._has.get);

    def div(self):
        e = 0
        for _, n in self._has.items():
            p = n / len(self.data)
            e = e - (p*math.log(p,2))
        return e

    def getColumnName(self):
        return self.name;
    
    def getColumnPosition(self):
        return self.at;

    def getData(self):
        return self.data;