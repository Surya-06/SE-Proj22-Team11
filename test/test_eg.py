"""
Run tests by running the following cmd in the root dir: py.test
"""

#Test case:1 'sym'

import sys 
from os import path


sys.path.append(path.dirname( path.dirname( path.abspath(__file__) )))

from Code.sym import *
from Code.num import *

def test():
    assert True;

def eg_sym():

    test_data = ["a","a","a","a","b","b","c"]
    column_name = 'Test Column 1'
    column_position = 1001

    expected_mode = 'a'
    expected_entropy = 1.379
    expected_freq_count = {'a': 4, 'b': 2, 'c': 1}

    test_sym_obj = Sym(column_position, column_name);
    for i in test_data:
        test_sym_obj.add(i)

    print("Validating eg sym");
    assert test_sym_obj._has == expected_freq_count
    assert expected_mode == test_sym_obj.mid()
    assert expected_entropy == round(test_sym_obj.div(), 3)

    assert column_name == test_sym_obj.getColumnName()
    assert column_position == test_sym_obj.getColumnPosition()

    
#Test case:2 'the'
def eg_the():
    print("Validating eg the");
    oo(the)
    return True

#Test case:3 'num'
def eg_num():
    the['nums'] = 110
    test_num_obj = Num()

    for i in range(1, 101):
        test_num_obj.add(i)

    mid = test_num_obj.mid()
    div = test_num_obj.div()

    print("Validing eg num");
    assert( mid>=50 and mid<=52)
    assert( div>30.5 and div<32)  
    
    
#Test case:4 'Bignum'   
def eg_Bignum():
    the['nums'] = 32
    test_num_obj = Num()

    for i in range(1, 1001):
        test_num_obj.add(i)
    
    print("Validating eg big num");
    if(32==len(test_num_obj._has)):
        assert(True)
    else:
        assert(False)
    
#HW2 Test cases
#Test case:1 eg.CSV
def eg_csv():
    n=0
    rows=csv("/data/auto93.csv")
    if (n<=10):
        oo(rows[n])
        n=n+1

#Test Case:2 eg.Data
#def eg_data():
    

#Test Case:3 eg.stats
#def eg_stats():


