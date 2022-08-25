"""
Run tests by running the following cmd in the root dir: py.test
"""

from main import increment, decrement

def test_increment():
    for i in range(1, 1000):
        assert increment(i) == i+1

def test_decrement():
    for i in range(1, 1000):
        assert decrement(i) == i-1

