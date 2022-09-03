"""
Run tests by running the following cmd in the root dir: py.test
"""

import sys
from Code.main import increment, decrement, square, divide
from Code.Classes.sym import Sym

# BEGIN - Old tests for CI sanity

def test_increment():
    for i in range(1, 1000):
        assert increment(i) == i+1

def test_decrement():
    for i in range(1, 1000):
        assert decrement(i) == i-1
        
def test_square():
    for i in range(1,1000):
        assert square(i) == i*i
        
def test_divide():
    for i in range(1, 1000):
        assert divide(i) == i/2

# END - Old tests for CI sanity

def test_sym_basic():
    test_symbol_map = {'a': 3, 'b': 5, 'c': 10, 'd': 1};
    test_data_expanded = list()
    for (key, value) in test_symbol_map.items():
        for i in range(1, value+1):
            test_data_expanded.append(key);

    column_name = 'Test Column 1';
    column_position = 1001;
    expected_mode = 'c' # repeated 10 times according to the map above.
    expected_entropy = 4 # 4 different items in the map above.
    
    test_num_obj = Sym(column_name, column_position);
    for i in test_data_expanded:
        test_num_obj.addData(i);

    assert column_name == test_num_obj.getColumnName();
    assert column_position == test_num_obj.getColumnPosition();
    assert expected_mode == test_num_obj.getMode();
    assert expected_entropy == test_num_obj.getEntropy();




