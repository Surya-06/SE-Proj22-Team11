# Rows class holds summaries of rows
import copy

class Rows:
    def __init__(self, t):
        self.cells = t
        self.cooked = copy.deepcopy(t)
        self.isEvaled = False
