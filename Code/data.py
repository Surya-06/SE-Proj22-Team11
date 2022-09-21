# Data holder class to contain all info fetched from the file

from enum import Enum
from cols import Cols
from utils import the, csv
from num import Num
from sym import Sym
from rows import Rows

class Data:
  def __init__(self, src):
    if the['data'] != '':
      raise Exception('RE-INITIALIZE ERROR: global data object already exists')
    the['data'] = self
    self.cols = None
    self.rows = []
    src = csv(src)
    for row in src:
      self.add(row)
  
  def add(self, xs):
    if not self.cols:
      self.cols = Cols(xs)
    else:
      row = Rows(xs) if type(xs) == list else xs
      self.rows.append(row)
      for todo in [self.cols.x, self.cols.y]:
        for col in todo:
          col.add(row.cells[col.at])
  
  def stats(self, places, showCols, fun):
    # showCols, fun = showCols or self.cols.y, fun or 'mid'
    # t = {}
    # for col in showCols:
      v = col.mid() if fun == 'mid' else col.div()
      v = round(v, places) if isinstance(v, float) else v
      t[col.name]=v
    return t