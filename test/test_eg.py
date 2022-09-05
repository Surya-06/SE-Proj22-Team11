"""
Run tests by running the following cmd in the root dir: py.test
"""

from Code.utils import *
from Code.main import the
from Code.sym import Sym
from Code.num import Num

def test_eg_sym():

    test_data = ["a","a","a","a","b","b","c"]
    column_name = 'Test Column 1'
    column_position = 1001

    expected_mode = 'a'
    expected_entropy = 1.379
    expected_freq_count = {'a': 4, 'b': 2, 'c': 1}

    test_sym_obj = Sym(column_position, column_name);
    for i in test_data:
        test_sym_obj.add(i)

    assert test_sym_obj._has == expected_freq_count
    assert expected_mode == test_sym_obj.mid()
    assert expected_entropy == round(test_sym_obj.div(), 3)

    assert column_name == test_sym_obj.getColumnName()
    assert column_position == test_sym_obj.getColumnPosition()

def test_eg_the():
    oo(the)
    return True

def test_eg_num():
    test_num_obj = Num()

    for i in range(1, 101):
        test_num_obj.add(i)

    mid = test_num_obj.mid()
    div = test_num_obj.div()

    assert( mid>=50 and mid<=52)
    assert( div>30.5 and div<32)     


