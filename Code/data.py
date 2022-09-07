# Data holder class to contain all info fetched from the file

from enum import Enum;

import utils;
from num import Num;
from sym import Sym;

class Data:
  def __init__(self, header_string: str):
    if utils.the['data'] != '':
      raise Exception('RE-INITIALIZE ERROR: global data object already exists')
    utils.the['data'] = self;
    self.columns = [];
    self.column_indices = [];
    self.__setupColumnStructureFromHeader__(header_string);

  def __addColumn__(self, name: str, position: int):
    new_column = '';

    # Uppercase columns are numeric data.
    if name.isupper():
      new_column = Num(position, name);
    else:
      new_column = Sym(position, name);
    
    self.columns.append(new_column);
    self.column_indices.append(position);
  
  def __setupColumnStructureFromHeader__(self, header_string: str):
    # TODO: + / - related handling.
    column_name = '';
    column_position = 0;
    for character in header_string:
      if character == ',':
        if len(column_name) > 0:
          self.__addColumn__(column_name, column_position);
          column_name = '';
          column_position += 1;
      elif character == ':':
        # skip column ending with :
        column_name = '';
        column_position += 1;
      else:
        column_name = column_name + character;
    self.__addColumn__(column_name, column_position);

  def importDataFromLine(self, csv_line: str):
    data_values = csv_line.split(',');
    print("csv line : " , data_values);
    for i in self.column_indices:
      self.columns[i].add(data_values[i]);
