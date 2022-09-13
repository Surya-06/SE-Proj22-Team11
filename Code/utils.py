# File for misc utilities
import math, re

the = {
    'data': '',
    'show_help': False,
    'filepath': '',
    'dump': False,
    'nums': 512,
    'seed': 10019,
    'seperator': ',',
    'eg': None
};


def per(t, p):
    p = math.floor(((p or .5)*len(t))+.5)
    return t[max(1,min(len(t),p))]

def oo(t):
    print(str(t))
    return t

def coerce(s):
    s = float(s) if bool(re.search(r'\d', s)) else s
    return s

def csv(src):
    if len(src.strip()) == 0:
        raise Exception('FILE PATH ERROR: File path not provided')
    rows = []
    with open(src, 'r', encoding='utf-8') as file:
        for row_no, line in enumerate(file):
            row = list(map(coerce, line.strip().split(the['seperator'])))
            rows.append(row)
    return rows