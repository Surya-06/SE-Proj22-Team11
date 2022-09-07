import sys, random

import utils

class Num:
    def __init__(self, c = 0, s = ''):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}
        self.lo = sys.maxsize
        self.hi = -sys.maxsize
        self.is_sorted = True
        self.w = -1 if self.name and self.name[-1] == '-' else 1

    def nums(self):
        if not self.is_sorted:
            dict(sorted(self._has.items()))
            self.is_sorted = True
        return self._has
    
    def add(self, v):
        if v != '?':
            v = int(v)
            self.n  += 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            pos = None
            if len(self._has) < utils.the['nums']:
                pos = 1 + len(self._has)
            elif random.randint(0, sys.maxsize) < utils.the['nums']/self.n:
                pos = random.randint(0, len(self._has))
            if pos:
                self.is_sorted = False
                self._has[pos] = v
    
    def div(self):
        a = self.nums()
        return (per(a,.9)-per(a,.1))/2.58
    
    def mid(self):
        return per(self.nums(),.5)