# Cols class holds summaries of columns

class Cols:
    def __init__(self, names: list):

        self.names = names
        self.all = {}
        self.klass = None
        self.x = {}
        self.y = {}

        for col_name in names:
            _type = ""
            if col_name[0].isupper():
                _type = "Num"
                self.all[col_name] = _type
            else:    
                _type = "Sym"
                self.all[col_name] = _type

            if not col_name[-1] == ":":
                if "-" in col_name or "+" in col_name:
                    self.y[col_name] = _type
                else:
                    self.x[col_name] = _type
