# File for misc utilities
import math

the = {
    'data': '',
    'show_help': False,
    'filepath': '',
    'dump': False,
    'nums': 512,
    'seed': 10019,
    'seperator': ','
};


def per(t, p):
    p = math.floor(((p or .5)*len(t))+.5)
    return t[max(1,min(len(t),p))]

def oo(t):
    print(str(t))
    return t