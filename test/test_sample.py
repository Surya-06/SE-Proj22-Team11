"""
Run tests by running the following cmd in the root dir: py.test
"""

import sys
from Code.main import increment, decrement, square

def test_increment():
    for i in range(1, 1000):
        assert increment(i) == i+1

def test_decrement():
    for i in range(1, 1000):
        assert decrement(i) == i-1

def test_square():
    for i in range(1,1000):
        assert sqaure(i)== i*i
