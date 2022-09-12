# Cols class holds summaries of columns
from unicodedata import name
from num import Num
from sym import Sym

class Cols:
    def __init__(self, names):

        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []

        for col_name in names:
            if col_name[0].isupper():
                col = Num(names.index(col_name), col_name)
            else:
                col = Sym(names.index(col_name), col_name)
            self.all.append(col)

            if not col_name[-1] == ":":
                if "-" in col_name or "+" in col_name or "!" in col_name:
                    self.y.append(col)
                else:
                    self.x.append(col)
                if "!" in col_name:
                    self.klass=col