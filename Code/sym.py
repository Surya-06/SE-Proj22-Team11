# SE HW - 2

class Sym:
    def __init__(self, column_name, column_position):
        self.column_name = column_name
        self.column_position = column_position
        self.data = list()
        self.freq_count = dict()

    def addData(self, value):
        self.data.append(value);
        if value in self.freq_count:
            self.freq_count[value]+=1;
        else:
            self.freq_count[value]=1;

    def getMode(self):
        return max(self.freq_count, key=self.freq_count.get);

    def getEntropy(self):
        return len(self.freq_count.keys());

    def getColumnName(self):
        return self.column_name;
    
    def getColumnPosition(self):
        return self.column_position;

    def getData(self):
        return self.data;




