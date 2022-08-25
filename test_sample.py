"""
Run tests by running the following cmd in the root dir: py.test
"""


def inc(x):
    return x + 1

def dec(x):
    return x - 1

def test_inc():
    for i in range(1, 10000):
        assert inc(i) == i+1

def test_dec():
    for i in range(1, 10000):
        assert dec(i) == i-1

