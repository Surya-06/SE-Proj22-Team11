
#Test case:1 'sym'

import sys 
from os import path
from pathlib import Path

# Add required paths to resolve imports
kTestFolderPath = str(Path(__file__).parent.absolute())
kCodeFolderPath = str(Path(Path(__file__).parent.parent/"Code").absolute());

sys.path.append(kTestFolderPath);
sys.path.append(kCodeFolderPath);

print()
print("updated value of sys.path : " , sys.path );

from Code.sym import *
from Code.num import *
from data import Data

def get_test_file_path():
    return Path(__file__).parent/"auto93.csv"

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
    print(":div {} :mid {}\n".format(expected_entropy, expected_mode))
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
    print(":div {} :mid {}\n".format(div, mid))
    assert( mid>=50 and mid<=52)
    assert( div>30.5 and div<32)  
    
#Test case:4 'Bignum'   
def eg_Bignum():
    the['nums'] = 32
    test_num_obj = Num()

    for i in range(1, 1001):
        test_num_obj.add(i)
    print("Validating eg big num");
    oo(test_num_obj.nums())
    if(32==len(test_num_obj._has)):
        assert(True)
    else:
        assert(False)
    print("\n")

#HW2 Test cases

#Test case:1 eg_CSV

def eg_csv():
    n=0
    filepath = get_test_file_path()
    rows=csv(filepath)
    print("Validating csv")
    while(n<=10):
        oo(rows[n])
        n=n+1
    print("\n")

#Test case:2 eg_Data
def eg_data():

    if the['data']:
        the['data'] = ''

    d = Data(get_test_file_path())
    print("Validating Data")
    for i in d.cols.y:
        print(":at {} , :hi {}, :is_sorted {}, :lo {}, :n {}, :name {}, :w {}\n".format( i.at, i.hi, i.is_sorted, i.lo, i.n, i.name,i.w))  

#Test case:3 eg_stats  

def eg_stats():
    
    if the['data']:
        the['data'] = ''

    data = Data(get_test_file_path())
    print("-------------------------------------------------------------------------")
    print("xmid  ", data.stats(2, data.cols.x, "mid"))
    print("xdiv  ", data.stats(3, data.cols.x, "div"))
    print("ymid  ", data.stats(1, data.cols.y, "mid"))
    print("ydiv  ", data.stats(3, data.cols.y, "div"))
    print("\n")

# Test case: eg_list

def eg_list():

    tests = ["eg_sym", "eg_the", "eg_num", "eg_Bignum", "eg_csv", "eg_data", "eg_stats"]
    print("All Tests:")
    for test in tests:
        print(test)
    print("\n")

# Test case: Run all test cases

def eg_all():  

    eg_list()
    eg_sym()
    eg_num()
    eg_Bignum()
    eg_csv()
    eg_data()
    eg_stats()
    eg_the()

def test_runner():
    print("Runner for automated hooks in github");
    eg_all();